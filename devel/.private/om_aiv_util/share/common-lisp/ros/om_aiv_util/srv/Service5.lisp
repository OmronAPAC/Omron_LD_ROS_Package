; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude Service5-request.msg.html

(cl:defclass <Service5-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:string
    :initform "")
   (b
    :reader b
    :initarg :b
    :type cl:string
    :initform "")
   (c
    :reader c
    :initarg :c
    :type cl:string
    :initform "")
   (d
    :reader d
    :initarg :d
    :type cl:string
    :initform "")
   (e
    :reader e
    :initarg :e
    :type cl:string
    :initform ""))
)

(cl:defclass Service5-request (<Service5-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service5-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service5-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service5-request> is deprecated: use om_aiv_util-srv:Service5-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Service5-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <Service5-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:b-val is deprecated.  Use om_aiv_util-srv:b instead.")
  (b m))

(cl:ensure-generic-function 'c-val :lambda-list '(m))
(cl:defmethod c-val ((m <Service5-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:c-val is deprecated.  Use om_aiv_util-srv:c instead.")
  (c m))

(cl:ensure-generic-function 'd-val :lambda-list '(m))
(cl:defmethod d-val ((m <Service5-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:d-val is deprecated.  Use om_aiv_util-srv:d instead.")
  (d m))

(cl:ensure-generic-function 'e-val :lambda-list '(m))
(cl:defmethod e-val ((m <Service5-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:e-val is deprecated.  Use om_aiv_util-srv:e instead.")
  (e m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service5-request>) ostream)
  "Serializes a message object of type '<Service5-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'a))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'b))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'b))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'c))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'c))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'd))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'e))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'e))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service5-request>) istream)
  "Deserializes a message object of type '<Service5-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'a) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'b) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'b) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'c) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'c) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'e) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'e) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service5-request>)))
  "Returns string type for a service object of type '<Service5-request>"
  "om_aiv_util/Service5Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service5-request)))
  "Returns string type for a service object of type 'Service5-request"
  "om_aiv_util/Service5Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service5-request>)))
  "Returns md5sum for a message object of type '<Service5-request>"
  "92b9e35a523fcf2c6affbc657156b6ea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service5-request)))
  "Returns md5sum for a message object of type 'Service5-request"
  "92b9e35a523fcf2c6affbc657156b6ea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service5-request>)))
  "Returns full string definition for message of type '<Service5-request>"
  (cl:format cl:nil "string a~%string b~%string c~%string d~%string e~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service5-request)))
  "Returns full string definition for message of type 'Service5-request"
  (cl:format cl:nil "string a~%string b~%string c~%string d~%string e~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service5-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'a))
     4 (cl:length (cl:slot-value msg 'b))
     4 (cl:length (cl:slot-value msg 'c))
     4 (cl:length (cl:slot-value msg 'd))
     4 (cl:length (cl:slot-value msg 'e))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service5-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service5-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
    (cl:cons ':c (c msg))
    (cl:cons ':d (d msg))
    (cl:cons ':e (e msg))
))
;//! \htmlinclude Service5-response.msg.html

(cl:defclass <Service5-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass Service5-response (<Service5-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service5-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service5-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service5-response> is deprecated: use om_aiv_util-srv:Service5-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <Service5-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service5-response>) ostream)
  "Serializes a message object of type '<Service5-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service5-response>) istream)
  "Deserializes a message object of type '<Service5-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'device) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'device) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service5-response>)))
  "Returns string type for a service object of type '<Service5-response>"
  "om_aiv_util/Service5Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service5-response)))
  "Returns string type for a service object of type 'Service5-response"
  "om_aiv_util/Service5Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service5-response>)))
  "Returns md5sum for a message object of type '<Service5-response>"
  "92b9e35a523fcf2c6affbc657156b6ea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service5-response)))
  "Returns md5sum for a message object of type 'Service5-response"
  "92b9e35a523fcf2c6affbc657156b6ea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service5-response>)))
  "Returns full string definition for message of type '<Service5-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service5-response)))
  "Returns full string definition for message of type 'Service5-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service5-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service5-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service5-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service5)))
  'Service5-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service5)))
  'Service5-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service5)))
  "Returns string type for a service object of type '<Service5>"
  "om_aiv_util/Service5")