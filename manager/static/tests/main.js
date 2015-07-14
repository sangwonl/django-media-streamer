var session = null;

if (!chrome.cast || !chrome.cast.isAvailable) {
  setTimeout(initializeCastApi, 1000);
}

function initializeCastApi() {
  var appID = '90CA4506';   // chrome.cast.media.DEFAULT_MEDIA_RECEIVER_APP_ID;
  var sessionRequest = new chrome.cast.SessionRequest(appID);
  var apiConfig = new chrome.cast.ApiConfig(sessionRequest, sessionListener, receiverListener);

  chrome.cast.initialize(apiConfig, onInitSuccess, onError);
}

function launchApp() {
  chrome.cast.requestSession(onRequestSessionSuccess, onLaunchError);
}

function doChromecast() {
  var videoSrc = document.getElementById('sample-video-src').getAttribute('src');
  loadAndPlayMedia(videoSrc);
}

function getContentType(url) {
  var contentType = 'video/mp4';
  var parts = url.split('.');
  if (!(parts.length === 1 || (parts[0] === '' && parts.length === 2))) {
    var extension = parts.pop().toLowerCase();
    if (extension === 'mpd') {
      contentType = 'application/dash+xml';
    }
    else if (extension === 'm3u8') {
      contentType = 'application/x-mpegurl';
    }
  }
  return contentType;
}

function loadAndPlayMedia(mediaURL) {
  var mediaInfo = new chrome.cast.media.MediaInfo(mediaURL);
  mediaInfo.metadata = new chrome.cast.media.GenericMediaMetadata();
  mediaInfo.metadata.metadataType = chrome.cast.media.MetadataType.GENERIC;
  mediaInfo.metadata.title = 'Hello World';
  mediaInfo.metadata.subtitle = 'Sub Title Here';
  mediaInfo.metadata.images = [new chrome.cast.Image('https://goo.gl/ZRMjjO')];
  mediaInfo.contentType = getContentType(mediaURL);

  var request = new chrome.cast.media.LoadRequest(mediaInfo);
  request.autoplay = true;
  request.currentTime = 0;

  session.loadMedia(request, onMediaSuccess, onMediaError);
}

// Callbacks
function onInitSuccess() {}
function onError(e) {}
function sessionListener(e) {session = e;}
function receiverListener(e) {}
function onMediaSuccess() {session.play();}
function onMediaError(e) {}
function onRequestSessionSuccess(e) {session = e;}
function onLaunchError(e) {}

