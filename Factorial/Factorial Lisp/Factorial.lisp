;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Factorial en Common Lisp
; Usando SBCL
; 
; @author Benedetto
; @date 2020/07/22
; @version 0.1
; Ejemplo de ejecución sbcl --script factorial.lisp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun factorial(n)(
    if (< n 2) 1 (* n factorial(- n 1))
))