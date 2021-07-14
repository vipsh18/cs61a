(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
  	((< num 0) -1)
	((> num 0) 1)
	(else 0))
)


(define (square x) (* x x))

(define (even x)
	(if (= (remainder x 2) 0)
	#t
	#f))

(define (odd x)
	(if (= (remainder x 2) 1)
	#t
	#f))

(define (pow x y)
	(cond
		((= y 2) (square x))
		((even? y) (square (pow x (/ k 2))))
		(odd? y (* x (square (pow x (/ k 2)))))
)
