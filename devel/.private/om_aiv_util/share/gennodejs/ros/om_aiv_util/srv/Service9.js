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
        this.b = '';
      }
      if (initObj.hasOwnProperty('c')) {
        this.c = initObj.c
      }
      else {
        this.c = '';
      }
      if (initObj.hasOwnProperty('d')) {
        this.d = initObj.d
      }
      else {
        this.d = '';
      }
      if (initObj.hasOwnProperty('e')) {
        this.e = initObj.e
      }
      else {
        this.e = '';
      }
      if (initObj.hasOwnProperty('f')) {
        this.f = initObj.f
      }
      else {
        this.f = '';
      }
      if (initObj.hasOwnProperty('g')) {
        this.g = initObj.g
      }
      else {
        this.g = '';
      }
      if (initObj.hasOwnProperty('h')) {
        this.h = initObj.h
      }
      else {
        this.h = '';
      }
      if (initObj.hasOwnProperty('i')) {
        this.i = initObj.i
      }
      else {
        this.i = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service9Request
    // Serialize message field [a]
    bufferOffset = _arraySerializer.string(obj.a, buffer, bufferOffset, null);
    // Serialize message field [b]
    bufferOffset = _serializer.string(obj.b, buffer, bufferOffset);
    // Serialize message field [c]
    bufferOffset = _serializer.string(obj.c, buffer, bufferOffset);
    // Serialize message field [d]
    bufferOffset = _serializer.string(obj.d, buffer, bufferOffset);
    // Serialize message field [e]
    bufferOffset = _serializer.string(obj.e, buffer, bufferOffset);
    // Serialize message field [f]
    bufferOffset = _serializer.string(obj.f, buffer, bufferOffset);
    // Serialize message field [g]
    bufferOffset = _serializer.string(obj.g, buffer, bufferOffset);
    // Serialize message field [h]
    bufferOffset = _serializer.string(obj.h, buffer, bufferOffset);
    // Serialize message field [i]
    bufferOffset = _serializer.string(obj.i, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service9Request
    let len;
    let data = new Service9Request(null);
    // Deserialize message field [a]
    data.a = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [b]
    data.b = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [c]
    data.c = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [d]
    data.d = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [e]
    data.e = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [f]
    data.f = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [g]
    data.g = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [h]
    data.h = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [i]
    data.i = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.a.forEach((val) => {
      length += 4 + val.length;
    });
    length += object.b.length;
    length += object.c.length;
    length += object.d.length;
    length += object.e.length;
    length += object.f.length;
    length += object.g.length;
    length += object.h.length;
    length += object.i.length;
    return length + 36;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/Service9Request';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7803b643a81fb2ac82d7377f398bdb7b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] a
    string b
    string c
    string d
    string e
    string f
    string g
    string h
    string i
    
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
      resolved.b = ''
    }

    if (msg.c !== undefined) {
      resolved.c = msg.c;
    }
    else {
      resolved.c = ''
    }

    if (msg.d !== undefined) {
      resolved.d = msg.d;
    }
    else {
      resolved.d = ''
    }

    if (msg.e !== undefined) {
      resolved.e = msg.e;
    }
    else {
      resolved.e = ''
    }

    if (msg.f !== undefined) {
      resolved.f = msg.f;
    }
    else {
      resolved.f = ''
    }

    if (msg.g !== undefined) {
      resolved.g = msg.g;
    }
    else {
      resolved.g = ''
    }

    if (msg.h !== undefined) {
      resolved.h = msg.h;
    }
    else {
      resolved.h = ''
    }

    if (msg.i !== undefined) {
      resolved.i = msg.i;
    }
    else {
      resolved.i = ''
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
        this.device = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service9Response
    // Serialize message field [device]
    bufferOffset = _serializer.string(obj.device, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service9Response
    let len;
    let data = new Service9Response(null);
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
    return 'om_aiv_util/Service9Response';
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
    const resolved = new Service9Response(null);
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
  Request: Service9Request,
  Response: Service9Response,
  md5sum() { return 'f7a77e900f56696065fc1ed66c979125'; },
  datatype() { return 'om_aiv_util/Service9'; }
};
