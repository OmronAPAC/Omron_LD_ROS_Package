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

class Service9Request {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
      this.b = null;
      this.c = null;
      this.d = null;
      this.e = null;
      this.f = null;
      this.g = null;
      this.h = null;
      this.i = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = [];
      }
      if (initObj.hasOwnProperty('b')) {
        this.b = initObj.b
      }
      else {
        this.b = [];
      }
      if (initObj.hasOwnProperty('c')) {
        this.c = initObj.c
      }
      else {
        this.c = [];
      }
      if (initObj.hasOwnProperty('d')) {
        this.d = initObj.d
      }
      else {
        this.d = [];
      }
      if (initObj.hasOwnProperty('e')) {
        this.e = initObj.e
      }
      else {
        this.e = [];
      }
      if (initObj.hasOwnProperty('f')) {
        this.f = initObj.f
      }
      else {
        this.f = [];
      }
      if (initObj.hasOwnProperty('g')) {
        this.g = initObj.g
      }
      else {
        this.g = [];
      }
      if (initObj.hasOwnProperty('h')) {
        this.h = initObj.h
      }
      else {
        this.h = [];
      }
      if (initObj.hasOwnProperty('i')) {
        this.i = initObj.i
      }
      else {
        this.i = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service9Request
    // Serialize message field [a]
    bufferOffset = _arraySerializer.string(obj.a, buffer, bufferOffset, null);
    // Serialize message field [b]
    bufferOffset = _arraySerializer.string(obj.b, buffer, bufferOffset, null);
    // Serialize message field [c]
    bufferOffset = _arraySerializer.string(obj.c, buffer, bufferOffset, null);
    // Serialize message field [d]
    bufferOffset = _arraySerializer.string(obj.d, buffer, bufferOffset, null);
    // Serialize message field [e]
    bufferOffset = _arraySerializer.string(obj.e, buffer, bufferOffset, null);
    // Serialize message field [f]
    bufferOffset = _arraySerializer.string(obj.f, buffer, bufferOffset, null);
    // Serialize message field [g]
    bufferOffset = _arraySerializer.string(obj.g, buffer, bufferOffset, null);
    // Serialize message field [h]
    bufferOffset = _arraySerializer.string(obj.h, buffer, bufferOffset, null);
    // Serialize message field [i]
    bufferOffset = _arraySerializer.string(obj.i, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service9Request
    let len;
    let data = new Service9Request(null);
    // Deserialize message field [a]
    data.a = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [b]
    data.b = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [c]
    data.c = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [d]
    data.d = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [e]
    data.e = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [f]
    data.f = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [g]
    data.g = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [h]
    data.h = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [i]
    data.i = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.a.forEach((val) => {
      length += 4 + val.length;
    });
    object.b.forEach((val) => {
      length += 4 + val.length;
    });
    object.c.forEach((val) => {
      length += 4 + val.length;
    });
    object.d.forEach((val) => {
      length += 4 + val.length;
    });
    object.e.forEach((val) => {
      length += 4 + val.length;
    });
    object.f.forEach((val) => {
      length += 4 + val.length;
    });
    object.g.forEach((val) => {
      length += 4 + val.length;
    });
    object.h.forEach((val) => {
      length += 4 + val.length;
    });
    object.i.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 36;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/Service9Request';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '791159f7045e778035dcbcbaa1bb29ec';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] a
    string[] b
    string[] c
    string[] d
    string[] e
    string[] f
    string[] g
    string[] h
    string[] i
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service9Request(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = []
    }

    if (msg.b !== undefined) {
      resolved.b = msg.b;
    }
    else {
      resolved.b = []
    }

    if (msg.c !== undefined) {
      resolved.c = msg.c;
    }
    else {
      resolved.c = []
    }

    if (msg.d !== undefined) {
      resolved.d = msg.d;
    }
    else {
      resolved.d = []
    }

    if (msg.e !== undefined) {
      resolved.e = msg.e;
    }
    else {
      resolved.e = []
    }

    if (msg.f !== undefined) {
      resolved.f = msg.f;
    }
    else {
      resolved.f = []
    }

    if (msg.g !== undefined) {
      resolved.g = msg.g;
    }
    else {
      resolved.g = []
    }

    if (msg.h !== undefined) {
      resolved.h = msg.h;
    }
    else {
      resolved.h = []
    }

    if (msg.i !== undefined) {
      resolved.i = msg.i;
    }
    else {
      resolved.i = []
    }

    return resolved;
    }
};

class Service9Response {
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
        this.device = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service9Response
    // Serialize message field [device]
    bufferOffset = _arraySerializer.string(obj.device, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service9Response
    let len;
    let data = new Service9Response(null);
    // Deserialize message field [device]
    data.device = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.device.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/Service9Response';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b91c71e89dd7ccb324fadf7f2ca2ad24';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] device
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service9Response(null);
    if (msg.device !== undefined) {
      resolved.device = msg.device;
    }
    else {
      resolved.device = []
    }

    return resolved;
    }
};

module.exports = {
  Request: Service9Request,
  Response: Service9Response,
  md5sum() { return '8f3b2965311f37d071bd387981e3ad17'; },
  datatype() { return 'om_aiv_util/Service9'; }
};
