// This File is for tracking the time across every page on the site
// code from https://saleemkce.github.io/timeonsite/docs/index.html


var config = {
    // track page by seconds. Default tracking is by milliseconds
    trackBy: 'seconds',
    callback: function(data) { /* callback denotes your data tracking is real-time */
        console.log(data);
        var endPointUrl = 'http://localhost:8000/track-tos/'; //Replace with your actual backend API URL
        if (data && data.trackingType) {
            if (data.trackingType == 'tos') {
                if (Tos.verifyData(data) != 'valid') {
                    console.log('Data abolished!');
                    return; 
                }
            }
    
            // make use of sendBeacon if this API is supported by your browser.
            if (navigator && typeof navigator.sendBeacon === 'function') {
                data.trasferredWith = 'sendBeacon';
                var blob = new Blob([JSON.stringify(data)], {type : 'application/json'});
                navigator.sendBeacon(endPointUrl, blob);
                }
            }
        }
    };
    var Tos;
    if (TimeOnSiteTracker) {
        Tos = new TimeOnSiteTracker(config);
}
