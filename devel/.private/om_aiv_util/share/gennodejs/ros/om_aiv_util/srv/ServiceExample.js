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

class ServiceExampleRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.onezero = null;
    }
    else {
      if (initObj.hasOwnProperty('onezero')) {
        this.onezero = initObj.onezero
      }
      else {
        this.onezero = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ServiceExampleRequest
    // Serialize message field [onezero]
    bufferOffset = _serializer.int32(obj.onezero, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ServiceExampleRequest
    let len;
    let data = new ServiceExampleRequest(null);
    // Deserialize message field [onezero]
    data.onezero = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/ServiceExampleRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5bd5e0f9ac4159bea0d24a22a826c13c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 onezero
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ServiceExampleRequest(null);
    if (msg.onezero !== undefined) {
      resolved.onezero = msg.onezero;
    }
    else {
      resolved.onezero = 0
    }

    return resolved;
    }
};

class ServiceExampleResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.turn = null;
    }
    else {
      if (initObj.hasOwnProperty('turn')) {
        this.turn = initObj.turn
      }
      else {
        this.turn = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ServiceExampleResponse
    // Serialize message field [turn]
    bufferOffset = _serializer.string(obj.turn, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ServiceExampleResponse
    let len;
    let data = new ServiceExampleResponse(null);
    // Deserialize message field [turn]
    data.turn = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.turn.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'om_aiv_util/ServiceExampleResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '318653ac5e682e6ac5a91ab3fcbcfd51';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string turn
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ServiceExampleResponse(null);
    if (msg.turn !== undefined) {
      resolved.turn = msg.turn;
    }
    else {
      resolved.turn = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: ServiceExampleRequest,
  Response: ServiceExampleResponse,
  md5sum() { return 'b6541b31be965d2ea76445e10907a742'; },
  datatype() { return 'om_aiv_util/ServiceExample'; }
};
