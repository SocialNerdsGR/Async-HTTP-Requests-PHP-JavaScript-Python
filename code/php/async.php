<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

$start = microtime(TRUE);

$promises = [];
for ($i = 1; $i < 10; $i++) {
    $promises[] = $client->requestAsync('GET', 'server:8000');
}

$responses = \GuzzleHttp\Promise\all($promises)->wait();

foreach ($responses as $response) {
    print($response->getBody() . PHP_EOL);
}

print('Time waiting: ' . (microtime(TRUE) - $start) . ' secs' . PHP_EOL);
