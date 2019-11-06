
(cl:in-package :asdf)

(defsystem "ld_services-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ServiceExample" :depends-on ("_package_ServiceExample"))
    (:file "_package_ServiceExample" :depends-on ("_package"))
  ))