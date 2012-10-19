<!--
Copyright (c) 2012 Christian Ertler.
All rights reserved. This program and the accompanying materials
are made available under the terms of the GNU Public License v3.0
which accompanies this distribution, and is available at
http://www.gnu.org/licenses/gpl.html

Contributors:
    Christian Ertler - initial API and implementation
-->

<!DOCTYPE html> 
<html>
	<head>
		<title>RhythmRemote</title>
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
				<h1>RhythmRemote</h1>
				<a class="ui-btn-right" id="queue_button" data-rel="popup" data-transition="pop" href="#queue_popup" data-icon="grid">Queue</a>
				<div id="queue_popup" data-role="popup" data-theme="a" data-position-to="origin" data-shadow="true" data-corners="true">
                    <ul id="queue_list" data-role="listview" data-inset="true" data-theme="b">
                        <li data-role="divider" data-theme="a" class="do_not_remove">Queue</li>
                </ul>
            </div>
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
                    <div class="song_information" style="display:none;">
                        <div>Now playing:</div>
                        <span class="song_information"></span>
                    </div>
                    <div style="width:150px;margin:auto;">
                        <label for="volumeSlider">Volume:</label>
                        <input class="volumeSlider" name="volumeSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
                    </div>
                    <div data-role="controlgroup" data-type="horizontal">
                        <a class="prevButton control_button"  href="#" data-rb-action="prev"  data-role="button">Previous</a>
                        <a class="playButton control_button"  href="#" data-rb-action="play"  data-role="button">Play</a>
                        <a class="pauseButton control_button" href="#" data-rb-action="pause" data-role="button">Pause</a>
                        <a class="stopButton control_button"  href="#" data-rb-action="stop"  data-role="button">Stop</a>
                        <a class="nextButton control_button"  href="#" data-rb-action="next"  data-role="button">Next</a>
                    </div>
                    <input class="seekSlider" type="range" min="0" max="100" data-highlight="true" data-mini="true" />
                </div>
			</div>
		</div>
	</body>
</html>
