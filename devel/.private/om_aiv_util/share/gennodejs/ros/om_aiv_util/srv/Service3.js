// Auto-generated. Do not edit!

// (in-package om_aiv_util.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class Service3Request {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
      this.b = null;
      this.c = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = '';
      }
      if (initObj.hasOwnProperty('b')) {
        this.b = initObj.b
      }
      else {
        this.b = '';
      }
      if (initObj.hasOwnProperty('c')) {
        this.c = initObj.c
      }
      else {
        this.c = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service3Request
    // Serialize message field [a]
    bufferOffset = _serializer.string(obj.a, buffer, bufferOffset);
    // Serialize message field [b]
    bufferOffset = _serializer.string(obj.b, buffer, bufferOffset);
    // Serialize message field [c]
    bufferOffset = _serializer.string(obj.c, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service3Request
    let len;
    let data = new Service3Request(null);
    // Deserialize message field [a]
    data.a = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [b]
    data.b = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [c]
    data.c = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.a.length;
    length += object.b.length;
    length += object.c.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/Service3Request';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'aedc855cb966317ef64c3818700a9db7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string a
    string b
    string c
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service3Request(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = ''
    }

    if (msg.b !== undefined) {
      resolved.b = msg.b;
    }
    else {
      resolved.b = ''
    }

    if (msg.c !== undefined) {
      resolved.c = msg.c;
    }
    else {
      resolved.c = ''
    }

    return resolved;
    }
};

class Service3Response {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.device = null;
    }
    else {
      if (initObj.hasOwnProperty('device')) {
        this.device = initObj.device
      }
      else {
        this.device = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service3Response
    // Serialize message field [device]
    bufferOffset = _serializer.string(obj.device, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service3Response
    let len;
    let data = new Service3Response(null);
    // Deserialize message field [device]
    data.device = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.device.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/Service3Response';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '25b143d1069c7861320973824c82b9d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string device
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service3Response(null);
    if (msg.device !== undefined) {
      resolved.device = msg.device;
    }
    else {
      resolved.device = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: Service3Request,
  Response: Service3Response,
  md5sum() { return '6d29793b95b92fdf3218d77308234efd'; },
  datatype() { return 'om_aiv_util/Service3'; }
};
