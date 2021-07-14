#lang racket

(define (sum-while initial-x condition add-to-total update-x)
	`(begin
		(define (f x total)
			(if ,condition
				(f ,update-x (+ total ,add-to-total))
				total))
		(f ,initial-x 0)))
(define result (sum-while 1 '(< (* x x) 50) 'x '(+ x 1)))
result
(eval result)