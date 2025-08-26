#lang racket

; Active Inference Implementation in Racket

(struct active-inference-agent
  (num-states num-observations num-actions
   beliefs a-matrix b-matrix c-vector d-vector))

(define (create-agent)
  (active-inference-agent
   4 3 2
   (vector 0.25 0.25 0.25 0.25)  ; beliefs
   (vector (vector 0.8 0.1 0.1)   ; a-matrix
           (vector 0.1 0.8 0.1)
           (vector 0.1 0.1 0.8))
   (vector (vector 0.9 0.1)       ; b-matrix
           (vector 0.1 0.9))
   (vector 0.0 0.5 0.0)            ; c-vector
   (vector 0.5 0.5)))              ; d-vector

(define (normalize-vector vec)
  (let ([total (for/sum ([v vec]) v)])
    (if (> total 0)
        (vector-map (λ (v) (/ v total)) vec)
        vec)))

(define (update-beliefs agent observation)
  (let* ([likelihood (vector-ref (active-inference-agent-a-matrix agent) 
                                 (sub1 observation))]
         [beliefs (active-inference-agent-beliefs agent)]
         [posterior (vector-map * likelihood beliefs)])
    (normalize-vector posterior)))

(define (calculate-expected-free-energy agent action)
  (for/sum ([belief (active-inference-agent-beliefs agent)])
    (if (> belief 0)
        (- (* belief (log belief)))
        0)))

(define (select-action agent)
  (define num-actions (active-inference-agent-num-actions agent))
  (define min-pair
    (for/fold ([min-pair (cons +inf.0 1)])
              ([action (in-range 1 (add1 num-actions))])
      (let ([efe (calculate-expected-free-energy agent action)])
        (if (< efe (car min-pair))
            (cons efe action)
            min-pair))))
  (cdr min-pair))

(define (step agent observation)
  (let ([new-beliefs (update-beliefs agent observation)])
    (struct-copy active-inference-agent agent [beliefs new-beliefs])))

(define (print-beliefs agent)
  (display "Beliefs: ")
  (define beliefs (active-inference-agent-beliefs agent))
  (for ([i (vector-length beliefs)])
    (printf "~.3f" (vector-ref beliefs i))
    (when (< i (sub1 (vector-length beliefs)))
      (display ", ")))
  (newline))

; Demo
(define (demo)
  (displayln "Racket Active Inference Demo")
  (define agent (create-agent))
  (display "Initial ")
  (print-beliefs agent)
  
  (for ([cycle (in-range 1 6)])
    (define observation (add1 (modulo (sub1 cycle) 3)))
    (define new-agent (step agent observation))
    (define action (select-action new-agent))
    (printf "Cycle ~a: Observation=~a, Action=~a, "
            cycle observation action)
    (print-beliefs new-agent)
    (set! agent new-agent)))

(demo)
