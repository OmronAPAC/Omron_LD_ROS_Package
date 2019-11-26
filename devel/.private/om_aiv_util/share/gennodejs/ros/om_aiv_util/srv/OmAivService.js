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

class OmAivServiceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OmAivServiceRequest
    // Serialize message field [a]
    bufferOffset = _arraySerializer.string(obj.a, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OmAivServiceRequest
    let len;
    let data = new OmAivServiceRequest(null);
    // Deserialize message field [a]
    data.a = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.a.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/OmAivServiceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4f6bc51cbf7510cc87897366558eca7b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] a
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OmAivServiceRequest(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = []
    }

    return resolved;
    }
};

class OmAivServiceResponse {
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
    // Serializes a message object of type OmAivServiceResponse
    // Serialize message field [device]
    bufferOffset = _serializer.string(obj.device, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OmAivServiceResponse
    let len;
    let data = new OmAivServiceResponse(null);
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
    return 'om_aiv_util/OmAivServiceResponse';
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
    const resolved = new OmAivServiceResponse(null);
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
  Request: OmAivServiceRequest,
  Response: OmAivServiceResponse,
  md5sum() { return 'b2778cec932742b2c8b6d125219e8d85'; },
  datatype() { return 'om_aiv_util/OmAivService'; }
};
