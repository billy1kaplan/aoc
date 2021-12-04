#lang racket

(require 2htdp/batch-io)

(define input-data (read-lines "inputs/day2.txt"))

(define make-location list) 
(define make-aim-location (lambda (d h a) (cons d (cons h a))))
(define get-depth car)
(define get-horizontal cadr)
(define get-aim cddr)

(define part1
  (lambda (directions)
    (let ([depth-horizontal
            (foldl (lambda (cur acc) 
                     (let* ([split-string (string-split cur)]
                            [direction (car split-string)]
                            [delta (string->number (cadr split-string))])
                       (cond [(equal? direction "forward")
                              (make-location
                                (get-depth acc)
                                (+ (get-horizontal acc) delta))]
                             [(equal? direction "down")
                              (make-location
                                (+ (get-depth acc) delta)
                                (get-horizontal acc))]
                             [(equal? direction "up")
                              (make-location
                                (- (get-depth acc) delta)
                                (get-horizontal acc))]
                              [#t (error "Unknown direction: ~a" direction)])))
                   (make-location 0 0)
                   directions)])
      (* (get-depth depth-horizontal)
         (get-horizontal depth-horizontal))
      )))

(define part2
  (lambda (directions)
    (let ([depth-horizontal
            (foldl (lambda (cur acc) 
                     (let* ([split-string (string-split cur)]
                            [direction (car split-string)]
                            [delta (string->number (cadr split-string))])
                       (cond [(equal? direction "forward")
                              (make-aim-location
                                (+ (get-depth acc)
                                   (* (get-aim acc) delta))
                                (+ (get-horizontal acc) delta)
                                (get-aim acc))]
                             [(equal? direction "down")
                              (make-aim-location
                                (get-depth acc)
                                (get-horizontal acc)
                                (+ (get-aim acc) delta))]
                             [(equal? direction "up")
                              (make-aim-location
                                (get-depth acc)
                                (get-horizontal acc)
                                (- (get-aim acc) delta))]
                              [#t (error "Unknown direction: ~a" direction)])))
                   (make-aim-location 0 0 0)
                   directions)])
      (* (get-depth depth-horizontal)
         (get-horizontal depth-horizontal))
      )))

(define assert-equal
  (lambda (a b)
    (if (not (eq? a b))
      (error "Expected ~a = ~b")
      'pass)))

(define test-data (list
                    "forward 5"
                    "down 5"
                    "forward 8"
                    "up 3"
                    "down 8"
                    "forward 2"))

(assert-equal (part1 test-data) 150)
(printf "Part 1: ~a\n" (part1 input-data))

(assert-equal (part2 test-data) 900)
(printf "Part 2: ~a\n" (part2 input-data))
