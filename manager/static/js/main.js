var CAST_API_INITIALIZATION_DELAY = 1000;

var session = null;

if (!chrome.cast || !chrome.cast.isAvailable) {
  setTimeout(initializeCastApi, CAST_API_INITIALIZATION_DELAY);
}

function initializeCastApi() {
  var appID = '90CA4506'; //chrome.cast.media.DEFAULT_MEDIA_RECEIVER_APP_ID;
  var sessionRequest = new chrome.cast.SessionRequest(appID);
  var apiConfig = new chrome.cast.ApiConfig(sessionRequest, sessionListener, receiverListener);

  chrome.cast.initialize(apiConfig, onInitSuccess, onError);
}

function onInitSuccess() {
}

function onError(e) {
}

function sessionListener(e) {
  session = e;
}

function receiverListener(e) {
}

function loadAndPlayMedia(mediaURL) {
  var mediaInfo = new chrome.cast.media.MediaInfo(mediaURL);
  mediaInfo.metadata = new chrome.cast.media.GenericMediaMetadata();
  mediaInfo.metadata.metadataType = chrome.cast.media.MetadataType.GENERIC;
  mediaInfo.metadata.title = 'Test Video';
  //mediaInfo.contentType = 'application/x-mpegURL';
  mediaInfo.contentType = 'video/mp4';

  var request = new chrome.cast.media.LoadRequest(mediaInfo);
  request.autoplay = true;
  request.currentTime = 0;

  session.loadMedia(request, onMediaSuccess, onMediaError);
}

function onMediaSuccess(e) {
  session.play();
}

function onMediaError(e) {
}

function launchApp() {
  chrome.cast.requestSession(onRequestSessionSuccess, onLaunchError);
}

function onRequestSessionSuccess(e) {
  session = e;
}

function onLaunchError(e) {
}

function doChromecast() {
  var videoSrc = document.getElementById('sample-video-src').getAttribute('src');
  loadAndPlayMedia(videoSrc);
}