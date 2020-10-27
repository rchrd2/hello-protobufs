<?php
$loader = require './vendor/autoload.php';

$loader->add('GPBMetadata\\', __DIR__.DIRECTORY_SEPARATOR.'compiled');
$loader->add('Tutorial\\', __DIR__.DIRECTORY_SEPARATOR.'compiled');

use Tutorial\Hello;

$hello = new Hello();
var_dump($hello);
echo $hello->getWho().PHP_EOL;
$hello->setWho("Richard");
echo $hello->getWho().PHP_EOL;
echo "Hello, {$hello->getWho()}!".PHP_EOL;

echo $hello->serializeToString().PHP_EOL;
echo $hello->serializeToJsonString().PHP_EOL;

$hello_copy = new Hello();
$hello_copy->mergeFromString($hello->serializeToString());
echo $hello_copy->serializeToJsonString().PHP_EOL;

$hello3 = new Hello();
$hello3->mergeFromJsonString($hello->serializeToJsonString());
echo $hello3->serializeToJsonString().PHP_EOL;

