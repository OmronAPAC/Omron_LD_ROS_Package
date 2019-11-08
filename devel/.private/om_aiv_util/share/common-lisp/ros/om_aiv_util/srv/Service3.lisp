; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude Service3-request.msg.html

(cl:defclass <Service3-request> (roslisp-msg-protocol:ros-message)
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
    :initform ""))
)

(cl:defclass Service3-request (<Service3-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service3-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service3-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service3-request> is deprecated: use om_aiv_util-srv:Service3-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Service3-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <Service3-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:b-val is deprecated.  Use om_aiv_util-srv:b instead.")
  (b m))

(cl:ensure-generic-function 'c-val :lambda-list '(m))
(cl:defmethod c-val ((m <Service3-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:c-val is deprecated.  Use om_aiv_util-srv:c instead.")
  (c m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service3-request>) ostream)
  "Serializes a message object of type '<Service3-request>"
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service3-request>) istream)
  "Deserializes a message object of type '<Service3-request>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service3-request>)))
  "Returns string type for a service object of type '<Service3-request>"
  "om_aiv_util/Service3Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service3-request)))
  "Returns string type for a service object of type 'Service3-request"
  "om_aiv_util/Service3Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service3-request>)))
  "Returns md5sum for a message object of type '<Service3-request>"
  "6d29793b95b92fdf3218d77308234efd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service3-request)))
  "Returns md5sum for a message object of type 'Service3-request"
  "6d29793b95b92fdf3218d77308234efd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service3-request>)))
  "Returns full string definition for message of type '<Service3-request>"
  (cl:format cl:nil "string a~%string b~%string c~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service3-request)))
  "Returns full string definition for message of type 'Service3-request"
  (cl:format cl:nil "string a~%string b~%string c~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service3-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'a))
     4 (cl:length (cl:slot-value msg 'b))
     4 (cl:length (cl:slot-value msg 'c))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service3-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service3-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
    (cl:cons ':c (c msg))
))
;//! \htmlinclude Service3-response.msg.html

(cl:defclass <Service3-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass Service3-response (<Service3-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service3-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service3-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service3-response> is deprecated: use om_aiv_util-srv:Service3-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <Service3-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service3-response>) ostream)
  "Serializes a message object of type '<Service3-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service3-response>) istream)
  "Deserializes a message object of type '<Service3-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service3-response>)))
  "Returns string type for a service object of type '<Service3-response>"
  "om_aiv_util/Service3Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service3-response)))
  "Returns string type for a service object of type 'Service3-response"
  "om_aiv_util/Service3Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service3-response>)))
  "Returns md5sum for a message object of type '<Service3-response>"
  "6d29793b95b92fdf3218d77308234efd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service3-response)))
  "Returns md5sum for a message object of type 'Service3-response"
  "6d29793b95b92fdf3218d77308234efd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service3-response>)))
  "Returns full string definition for message of type '<Service3-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service3-response)))
  "Returns full string definition for message of type 'Service3-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service3-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service3-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service3-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service3)))
  'Service3-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service3)))
  'Service3-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service3)))
  "Returns string type for a service object of type '<Service3>"
  "om_aiv_util/Service3")