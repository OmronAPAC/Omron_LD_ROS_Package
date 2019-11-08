; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude Service2-request.msg.html

(cl:defclass <Service2-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:string
    :initform "")
   (b
    :reader b
    :initarg :b
    :type cl:string
    :initform ""))
)

(cl:defclass Service2-request (<Service2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service2-request> is deprecated: use om_aiv_util-srv:Service2-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Service2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <Service2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:b-val is deprecated.  Use om_aiv_util-srv:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service2-request>) ostream)
  "Serializes a message object of type '<Service2-request>"
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service2-request>) istream)
  "Deserializes a message object of type '<Service2-request>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service2-request>)))
  "Returns string type for a service object of type '<Service2-request>"
  "om_aiv_util/Service2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service2-request)))
  "Returns string type for a service object of type 'Service2-request"
  "om_aiv_util/Service2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service2-request>)))
  "Returns md5sum for a message object of type '<Service2-request>"
  "4f7d11ca1dbd936717b1bb3469c922e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service2-request)))
  "Returns md5sum for a message object of type 'Service2-request"
  "4f7d11ca1dbd936717b1bb3469c922e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service2-request>)))
  "Returns full string definition for message of type '<Service2-request>"
  (cl:format cl:nil "string a~%string b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service2-request)))
  "Returns full string definition for message of type 'Service2-request"
  (cl:format cl:nil "string a~%string b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service2-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'a))
     4 (cl:length (cl:slot-value msg 'b))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service2-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
;//! \htmlinclude Service2-response.msg.html

(cl:defclass <Service2-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass Service2-response (<Service2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service2-response> is deprecated: use om_aiv_util-srv:Service2-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <Service2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service2-response>) ostream)
  "Serializes a message object of type '<Service2-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service2-response>) istream)
  "Deserializes a message object of type '<Service2-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service2-response>)))
  "Returns string type for a service object of type '<Service2-response>"
  "om_aiv_util/Service2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service2-response)))
  "Returns string type for a service object of type 'Service2-response"
  "om_aiv_util/Service2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service2-response>)))
  "Returns md5sum for a message object of type '<Service2-response>"
  "4f7d11ca1dbd936717b1bb3469c922e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service2-response)))
  "Returns md5sum for a message object of type 'Service2-response"
  "4f7d11ca1dbd936717b1bb3469c922e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service2-response>)))
  "Returns full string definition for message of type '<Service2-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service2-response)))
  "Returns full string definition for message of type 'Service2-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service2-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service2-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service2)))
  'Service2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service2)))
  'Service2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service2)))
  "Returns string type for a service object of type '<Service2>"
  "om_aiv_util/Service2")