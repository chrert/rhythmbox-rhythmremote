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
			$(document).bind("pagechange", function() {
				initialize();
				
				var updater = new playerInfoUpdater(true);
				updater.update();
				updateTimer = $.timer(function() {
					updater.update();
				}, 1000, true);
			});
			
			$(document).bind("pageload", function() {
				(new playerInfoUpdater(false)).update();
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
				
				<div style="margin-top:20px">		
				%include
				</div>
			</div>
			<div data-role="footer" data-id="playerControl" data-position="fixed">
                 <div style="margin:auto;text-align:center;" data-id="playerControl">
                    <div style="width:150px;margin:auto;">
                        <label for="volumeSlider">Volume:</label>
                        <input class="volumeSlider" name="volumeSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
                    </div>
                    <div data-role="controlgroup" data-type="horizontal">
                        <a class="prevButton" href="/prev" data-role="button">Previous</a>
                        <a class="playButton" href="/play" data-role="button">Play</a>
                        <a class="pauseButton" href="/pause" data-role="button">Pause</a>
                        <a class="stopButton" href="/sop" data-role="button">Stop</a>
                        <a class="nextButton" href="/next" data-role="button">Next</a>
                    </div>
                    <input class="seekSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
                </div>
			</div>
		</div>
	</body>
</html>