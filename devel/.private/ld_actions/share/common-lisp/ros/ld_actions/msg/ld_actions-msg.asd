
(cl:in-package :asdf)

(defsystem "ld_actions-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "DockAction" :depends-on ("_package_DockAction"))
    (:file "_package_DockAction" :depends-on ("_package"))
    (:file "DockActionFeedback" :depends-on ("_package_DockActionFeedback"))
    (:file "_package_DockActionFeedback" :depends-on ("_package"))
    (:file "DockActionGoal" :depends-on ("_package_DockActionGoal"))
    (:file "_package_DockActionGoal" :depends-on ("_package"))
    (:file "DockActionResult" :depends-on ("_package_DockActionResult"))
    (:file "_package_DockActionResult" :depends-on ("_package"))
    (:file "DockFeedback" :depends-on ("_package_DockFeedback"))
    (:file "_package_DockFeedback" :depends-on ("_package"))
    (:file "DockGoal" :depends-on ("_package_DockGoal"))
    (:file "_package_DockGoal" :depends-on ("_package"))
    (:file "DockResult" :depends-on ("_package_DockResult"))
    (:file "_package_DockResult" :depends-on ("_package"))
  ))