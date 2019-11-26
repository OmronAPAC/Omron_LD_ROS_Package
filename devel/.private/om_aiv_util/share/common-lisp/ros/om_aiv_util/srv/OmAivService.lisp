; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude OmAivService-request.msg.html

(cl:defclass <OmAivService-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass OmAivService-request (<OmAivService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OmAivService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OmAivService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<OmAivService-request> is deprecated: use om_aiv_util-srv:OmAivService-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <OmAivService-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OmAivService-request>) ostream)
  "Serializes a message object of type '<OmAivService-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'a))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OmAivService-request>) istream)
  "Deserializes a message object of type '<OmAivService-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'a) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'a)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OmAivService-request>)))
  "Returns string type for a service object of type '<OmAivService-request>"
  "om_aiv_util/OmAivServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OmAivService-request)))
  "Returns string type for a service object of type 'OmAivService-request"
  "om_aiv_util/OmAivServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OmAivService-request>)))
  "Returns md5sum for a message object of type '<OmAivService-request>"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OmAivService-request)))
  "Returns md5sum for a message object of type 'OmAivService-request"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OmAivService-request>)))
  "Returns full string definition for message of type '<OmAivService-request>"
  (cl:format cl:nil "string[] a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OmAivService-request)))
  "Returns full string definition for message of type 'OmAivService-request"
  (cl:format cl:nil "string[] a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OmAivService-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'a) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OmAivService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'OmAivService-request
    (cl:cons ':a (a msg))
))
;//! \htmlinclude OmAivService-response.msg.html

(cl:defclass <OmAivService-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass OmAivService-response (<OmAivService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OmAivService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OmAivService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<OmAivService-response> is deprecated: use om_aiv_util-srv:OmAivService-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <OmAivService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OmAivService-response>) ostream)
  "Serializes a message object of type '<OmAivService-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OmAivService-response>) istream)
  "Deserializes a message object of type '<OmAivService-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OmAivService-response>)))
  "Returns string type for a service object of type '<OmAivService-response>"
  "om_aiv_util/OmAivServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OmAivService-response)))
  "Returns string type for a service object of type 'OmAivService-response"
  "om_aiv_util/OmAivServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OmAivService-response>)))
  "Returns md5sum for a message object of type '<OmAivService-response>"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OmAivService-response)))
  "Returns md5sum for a message object of type 'OmAivService-response"
  "b2778cec932742b2c8b6d125219e8d85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OmAivService-response>)))
  "Returns full string definition for message of type '<OmAivService-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OmAivService-response)))
  "Returns full string definition for message of type 'OmAivService-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OmAivService-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OmAivService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'OmAivService-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'OmAivService)))
  'OmAivService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'OmAivService)))
  'OmAivService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OmAivService)))
  "Returns string type for a service object of type '<OmAivService>"
  "om_aiv_util/OmAivService")