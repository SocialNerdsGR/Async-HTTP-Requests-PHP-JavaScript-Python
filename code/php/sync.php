<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

$start = microtime(TRUE);

for ($i = 1; $i < 10; $i++) {
    $response = $client->request('GET', 'server:8000');
    print($response->getBody() . PHP_EOL);
}

print('Time waiting: ' . (microtime(TRUE) - $start) . ' secs' . PHP_EOL);
