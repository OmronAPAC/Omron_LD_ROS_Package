; Auto-generated. Do not edit!


(cl:in-package ld_services-srv)


;//! \htmlinclude ServiceExample-request.msg.html

(cl:defclass <ServiceExample-request> (roslisp-msg-protocol:ros-message)
  ((onezero
    :reader onezero
    :initarg :onezero
    :type cl:integer
    :initform 0))
)

(cl:defclass ServiceExample-request (<ServiceExample-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ServiceExample-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ServiceExample-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ld_services-srv:<ServiceExample-request> is deprecated: use ld_services-srv:ServiceExample-request instead.")))

(cl:ensure-generic-function 'onezero-val :lambda-list '(m))
(cl:defmethod onezero-val ((m <ServiceExample-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ld_services-srv:onezero-val is deprecated.  Use ld_services-srv:onezero instead.")
  (onezero m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ServiceExample-request>) ostream)
  "Serializes a message object of type '<ServiceExample-request>"
  (cl:let* ((signed (cl:slot-value msg 'onezero)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ServiceExample-request>) istream)
  "Deserializes a message object of type '<ServiceExample-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'onezero) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ServiceExample-request>)))
  "Returns string type for a service object of type '<ServiceExample-request>"
  "ld_services/ServiceExampleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ServiceExample-request)))
  "Returns string type for a service object of type 'ServiceExample-request"
  "ld_services/ServiceExampleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ServiceExample-request>)))
  "Returns md5sum for a message object of type '<ServiceExample-request>"
  "b6541b31be965d2ea76445e10907a742")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ServiceExample-request)))
  "Returns md5sum for a message object of type 'ServiceExample-request"
  "b6541b31be965d2ea76445e10907a742")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ServiceExample-request>)))
  "Returns full string definition for message of type '<ServiceExample-request>"
  (cl:format cl:nil "int32 onezero~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ServiceExample-request)))
  "Returns full string definition for message of type 'ServiceExample-request"
  (cl:format cl:nil "int32 onezero~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ServiceExample-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ServiceExample-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ServiceExample-request
    (cl:cons ':onezero (onezero msg))
))
;//! \htmlinclude ServiceExample-response.msg.html

(cl:defclass <ServiceExample-response> (roslisp-msg-protocol:ros-message)
  ((turn
    :reader turn
    :initarg :turn
    :type cl:string
    :initform ""))
)

(cl:defclass ServiceExample-response (<ServiceExample-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ServiceExample-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ServiceExample-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ld_services-srv:<ServiceExample-response> is deprecated: use ld_services-srv:ServiceExample-response instead.")))

(cl:ensure-generic-function 'turn-val :lambda-list '(m))
(cl:defmethod turn-val ((m <ServiceExample-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ld_services-srv:turn-val is deprecated.  Use ld_services-srv:turn instead.")
  (turn m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ServiceExample-response>) ostream)
  "Serializes a message object of type '<ServiceExample-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'turn))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'turn))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ServiceExample-response>) istream)
  "Deserializes a message object of type '<ServiceExample-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turn) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'turn) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ServiceExample-response>)))
  "Returns string type for a service object of type '<ServiceExample-response>"
  "ld_services/ServiceExampleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ServiceExample-response)))
  "Returns string type for a service object of type 'ServiceExample-response"
  "ld_services/ServiceExampleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ServiceExample-response>)))
  "Returns md5sum for a message object of type '<ServiceExample-response>"
  "b6541b31be965d2ea76445e10907a742")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ServiceExample-response)))
  "Returns md5sum for a message object of type 'ServiceExample-response"
  "b6541b31be965d2ea76445e10907a742")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ServiceExample-response>)))
  "Returns full string definition for message of type '<ServiceExample-response>"
  (cl:format cl:nil "string turn~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ServiceExample-response)))
  "Returns full string definition for message of type 'ServiceExample-response"
  (cl:format cl:nil "string turn~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ServiceExample-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'turn))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ServiceExample-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ServiceExample-response
    (cl:cons ':turn (turn msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ServiceExample)))
  'ServiceExample-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ServiceExample)))
  'ServiceExample-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ServiceExample)))
  "Returns string type for a service object of type '<ServiceExample>"
  "ld_services/ServiceExample")