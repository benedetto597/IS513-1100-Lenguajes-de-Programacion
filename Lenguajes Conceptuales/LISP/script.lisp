;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ejemplo de programa con Common Lisp
; Usando SBCL
; 
; @author Benedetto
; @date 2020/07/22
; @version 0.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Mensaje de bienvenida
(write-line "")
(write-line "")
(write-line "Escriba en pantalla un dato númerico")
(write-line "")

;Definir una variable y se le solicita el dato al usuario
(defvar "unaVariableCualquiera")
(setf "unaVariableCualquiera" (read))
(write-line "")

;Se imprimen los resultados de una operacion cualquiera
(write-line "El resultado de su número * 5 es: ")
(write (* 5 "unaVariableCualquiera))
(write-line "")
