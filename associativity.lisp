; ACL2 code to prove associativity

(include-book "std/osets/top" :dir :system)

(defun rimu (A B k)
    (if (= (len A) 0)
        B
        (if (= (len B) 0)
            A
            ; TODO
            (rimu A B k)
        )
    )
)
