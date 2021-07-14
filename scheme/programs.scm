#lang racket

(define (average x y)
	(/ (+ x y) 2))

(define (square x)
	(* x x))

(define (fib n)
	(if (<= n 1)
		n
		(+ (fib (- n 1)) (fib (- n 2)))))

(define (fact x)
	(if (<= x 1)
		1
		(* x (fact (- x 1)))))

(define (pow x y)
	(if (= y 2)
		(square x)
		(* x (pow x (- y 1)))))

(define (faster-pow x y)
	(cond
		((= y 2) (square x))
		((even? y) (square (faster-pow x (quotient y 2))))
		(odd? y (* x (square (faster-pow x (quotient y 2)))))
	)
)

(define (sum-evens s)
	(if (null? s)
	0
	(if (even? (car s))
		(+ (car s) (sum-evens  (cdr s)))
		(sum-evens (cdr s)))))

(define (append-list a b)
	(define x ))
(append-list '(1 2 3) '(2 3 4))

(define (print-out-list a)
	(if (empty? a)
		null
		((display (first a))
		(print-out-list (rest a)))))
(print-out-list '(1 2 3))