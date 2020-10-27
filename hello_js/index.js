const hello_pb = require("./compiled/hello_pb");

const hello = new hello_pb.Hello();

console.log(`Hello, ${hello.getWho()}!`);

hello.setWho("Richard");
console.log(`Hello, ${hello.getWho()}!`);

console.log(hello.toObject());

console.log(hello.serializeBinary());