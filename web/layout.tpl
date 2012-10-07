<!DOCTYPE html> 
<html>
	<head>
		<title>Rhythmwebfork</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" type="text/css" href="/script/jquery.mobile/jquery.mobile-1.2.0.min.css" />
		<style>
		    input.ui-slider-input {
	           display:none !important;
	        }
		</style>
		<script src="/script/jquery-1.8.2.min.js"></script>
		<script src="/script/jquery.mobile/jquery.mobile-1.2.0.min.js"></script>
		<script src="/script/jquery.timer.js"></script>
		<script src="/script/rbplayer.js"></script>
		<script>
		    var updateTimer;
			$(document).bind("pageshow", function() {
				initialize();
				
				var updater = new playerInfoUpdater();
				updater.update();
				updateTimer = $.timer(function() {
					updater.update();
				}, 1000, true);
			});
			
			$(document).bind("pagebeforechange", function() {
				if (typeof updateTimer != "undefined") {
				    updateTimer.stop();
				}
			});
		</script>
	</head>
	<body>
		<div data-role="page">
			<div data-role="header">
				%if defined('backlink'):
				<a data-transition="slidefade" data-direction="reverse" data-icon="back" href="{{backlink[0]}}">{{backlink[1]}}</a>
				%end
				<h1>Rhythmwebfork</h1>
			</div>
			
			<div data-role="content">
				<div data-role="popup" id="popupTooltip" class="ui-content" data-theme="e" style="max-width:350px;">
          			<p class="tooltip_content"></p>
				</div>
				
				<div style="margin:auto;text-align:center;">
				    <div style="width:150px;margin:auto;">
						<label for="volumeSlider">Volume:</label>
		                <input id="volumeSlider" name="volumeSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
	                </div>
					<div data-role="controlgroup" data-type="horizontal">
					    <a id="prevButton" href="#" data-role="button">Previous</a>
						<a id="playButton" href="#" data-role="button">Play</a>
						<a id="pauseButton" href="#" data-role="button">Pause</a>
						<a id="stopButton" href="#" data-role="button">Stop</a>
						<a id="nextButton" href="#" data-role="button">Next</a>
					</div>
					<input id="seekSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
				</div>
				<div style="margin-top:20px">		
				%include
				</div>
			</div>
		</div>
	</body>
</html>