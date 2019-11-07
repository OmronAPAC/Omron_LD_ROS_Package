; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude Service-request.msg.html

(cl:defclass <Service-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:string
    :initform ""))
)

(cl:defclass Service-request (<Service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service-request> is deprecated: use om_aiv_util-srv:Service-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service-request>) ostream)
  "Serializes a message object of type '<Service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'a))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service-request>) istream)
  "Deserializes a message object of type '<Service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'a) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service-request>)))
  "Returns string type for a service object of type '<Service-request>"
  "om_aiv_util/ServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service-request)))
  "Returns string type for a service object of type 'Service-request"
  "om_aiv_util/ServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service-request>)))
  "Returns md5sum for a message object of type '<Service-request>"
  "9965534556d6f239219ba39e543ce36b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service-request)))
  "Returns md5sum for a message object of type 'Service-request"
  "9965534556d6f239219ba39e543ce36b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service-request>)))
  "Returns full string definition for message of type '<Service-request>"
  (cl:format cl:nil "string a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service-request)))
  "Returns full string definition for message of type 'Service-request"
  (cl:format cl:nil "string a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'a))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service-request
    (cl:cons ':a (a msg))
))
;//! \htmlinclude Service-response.msg.html

(cl:defclass <Service-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass Service-response (<Service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service-response> is deprecated: use om_aiv_util-srv:Service-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <Service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service-response>) ostream)
  "Serializes a message object of type '<Service-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service-response>) istream)
  "Deserializes a message object of type '<Service-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service-response>)))
  "Returns string type for a service object of type '<Service-response>"
  "om_aiv_util/ServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service-response)))
  "Returns string type for a service object of type 'Service-response"
  "om_aiv_util/ServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service-response>)))
  "Returns md5sum for a message object of type '<Service-response>"
  "9965534556d6f239219ba39e543ce36b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service-response)))
  "Returns md5sum for a message object of type 'Service-response"
  "9965534556d6f239219ba39e543ce36b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service-response>)))
  "Returns full string definition for message of type '<Service-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service-response)))
  "Returns full string definition for message of type 'Service-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service)))
  'Service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service)))
  'Service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service)))
  "Returns string type for a service object of type '<Service>"
  "om_aiv_util/Service")