
(cl:in-package :asdf)

(defsystem "om_aiv_util-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "OmAivService" :depends-on ("_package_OmAivService"))
    (:file "_package_OmAivService" :depends-on ("_package"))
  ))