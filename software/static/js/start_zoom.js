var sdkKey = $('input[name=sdkKey]').val();
var signature = $('input[name=signature]').val();
var meetingNumber = $('input[name=meetingNumber]').val();
var zoomProfile = $('input[name=zoomProfile]').val();
var passWord = $('input[name=passWord]').val();


ZoomMtg.preLoadWasm()
ZoomMtg.prepareWebSDK()
// loads language files, also passes any error messages to the ui
ZoomMtg.i18n.load('en-US')
ZoomMtg.i18n.reload('en-US')

ZoomMtg.setZoomJSLib('../node_modules/@zoomus/websdk/dist/lib', '/av')
// ZoomMtg.setZoomJSLib('https://source.zoom.us/2.4.5/lib', '/av')


var signature = signature
var sdkKey = sdkKey
var meetingNumber = meetingNumber
var leaveUrl = 'http://127.0.0.1:8000/'
var userName = zoomProfile
var passWord = passWord
//var userEmail = ''

function startMeeting(signature) {

  document.getElementById('zmmtg-root').style.display = 'block'

  ZoomMtg.init({
    leaveUrl: leaveUrl,
    success: (success) => {
      console.log(success)
      ZoomMtg.join({
        signature: signature,
        sdkKey: sdkKey,
        meetingNumber: meetingNumber,
        userName: userName,
        passWord: passWord,
        // userEmail: userEmail,
        // tk: registrantToken,
        success: (success) => {
          console.log(success)
        },
        error: (error) => {
          console.log(error)
        },
      })
    },
    error: (error) => {
      console.log(error)
    }
  })
}

startMeeting(signature)
