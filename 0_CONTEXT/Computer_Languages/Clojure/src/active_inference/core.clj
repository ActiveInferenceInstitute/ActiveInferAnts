(ns active-inference.core
  (:require [clojure.core.matrix :as m]
            [clojure.core.matrix.operators :as ops]))

;; Configuration constants
(def num-states 4)
(def num-observations 3)
(def num-actions 2)

;; Create generative model components
(defn create-generative-model
  "Initialize A, B, C, D matrices for the generative model"
  []
  {:A (m/matrix [[0.8 0.1 0.1]   ; P(o=1|s)
                 [0.1 0.8 0.1]   ; P(o=2|s)
                 [0.1 0.1 0.8]]) ; P(o=3|s)
   :B (m/matrix [[0.9 0.1]       ; P(s'|s=1,a)
                 [0.1 0.9]])     ; P(s'|s=2,a)
   :C (m/matrix [0.0 0.5 0.0])   ; Preferred observations
   :D (m/matrix [0.5 0.5])})    ; Prior beliefs

(defn normalize-vector
  "Normalize a vector to sum to 1"
  [v]
  (let [sum (m/esum v)]
    (if (> sum 0)
      (ops// v sum)
      (m/div v (count v)))))

(defn update-beliefs
  "Update beliefs using Bayesian inference: P(s|o) ∝ P(o|s) * P(s)"
  [beliefs observation generative-model]
  (let [likelihood (m/get-row (:A generative-model) (dec observation))
        posterior (ops/* likelihood beliefs)]
    (normalize-vector posterior)))

(defn calculate-expected-free-energy
  "Calculate expected free energy for a given action"
  [beliefs action generative-model]
  (let [B (:B generative-model)
        future-beliefs (m/mmul B (m/get-column B action))
        future-beliefs (normalize-vector future-beliefs)]
    (->> (map #(let [p-s (m/mget beliefs %)
                     q-s (m/mget future-beliefs %)]
                 (if (> q-s 0)
                   (* p-s (- (Math/log p-s) (Math/log q-s)))
                   0))
             (range (m/row-count beliefs)))
         (reduce +))))

(defn select-action
  "Select action that minimizes expected free energy"
  [beliefs generative-model]
  (->> (range num-actions)
       (map #(vector % (calculate-expected-free-energy beliefs % generative-model)))
       (sort-by second)
       first
       first))

(defn perception-action-cycle
  "Complete perception-action cycle"
  [beliefs observation generative-model]
  (let [new-beliefs (update-beliefs beliefs observation generative-model)
        action (select-action new-beliefs generative-model)]
    {:beliefs new-beliefs
     :action action}))

(defn initialize-agent
  "Initialize agent with default parameters"
  []
  {:beliefs (normalize-vector (m/matrix (repeat num-states 1.0)))
   :generative-model (create-generative-model)})

(defn run-simulation
  "Run active inference simulation for specified steps"
  [steps]
  (loop [step 0
         agent (initialize-agent)
         observations (cycle [1 2 3 1 2])]
    (if (>= step steps)
      agent
      (let [observation (nth observations step)
            result (perception-action-cycle (:beliefs agent) observation (:generative-model agent))]
        (println (str "Step " step ":"))
        (println (str "  Observation: " observation))
        (println (str "  Beliefs: " (vec (m/to-vector (:beliefs result)))))
        (println (str "  Action: " (:action result)))
        (println)
        (recur (inc step)
               {:beliefs (:beliefs result)
                :generative-model (:generative-model agent)}
               observations)))))

(defn -main
  "Main entry point for the application"
  [& args]
  (println "Clojure Active Inference Demo")
  (println "============================")
  (run-simulation 10)
  (println "Simulation completed!"))
