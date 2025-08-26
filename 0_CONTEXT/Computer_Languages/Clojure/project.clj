(defproject active-inference "1.0.0"
  :description "Active Inference implementation in Clojure"
  :url "https://github.com/your-repo/active-inference-clojure"
  :license {:name "MIT"
            :url "https://opensource.org/licenses/MIT"}
  :dependencies [[org.clojure/clojure "1.11.1"]
                 [net.mikera/core.matrix "0.63.0"]
                 [net.mikera/vectorz-clj "0.48.0"]]
  :main active-inference.core
  :profiles {:dev {:dependencies [[org.clojure/tools.namespace "1.3.0"]]}})
