const CACHE_NAME = '1';
const urlsToCache = [
'/',
];
// Install event -cache assets
self.addEventListener('install', event => {
event.waituntil(
caches.open(CACHE_NAME)
.then(cache => {
return cache.addAll(urlsToCache);
})
);
});