function initialize() {
	$(".ui-page-active a.popup_select_link").click(function() {
		var entry_id = $(this).data("rb-entry-id");
		$("#popup_select_" + entry_id).popup("open", {
			transition : "pop"
		});
	});
	
	$(".ui-page-active a.track_link").click(
			function() {
				var $link = $(this);
				var entry_id = $link.data("rb-entry-id");
				$.ajax({
					url : "/play/" + entry_id,
					type : "GET"
				}).success(
						function() {
							$("#popup_select_" + entry_id).popup("close");
							var entry_name = $link.data("rb-entry-name");
							$("#popupTooltip > p.tooltip_content").text(
									"Now playing: " + entry_name);
							$("#popupTooltip").popup("open", {
								transition : "pop"
							});
						});
			});
	
	$(".ui-page-active #popupTooltip").popup({
		history : false,
		positionTo : "window"
	});
}

function playerInfoUpdater(activePage) {
	if (activePage === true) {
		var jqPrefix = ".ui-page-active ";
	} else {
		jqPrefix = "";
	}
	
	this.updateVolume = true;
	this.updatePosition = true;
	
	var updater = this;
	
	var $playButton = $(jqPrefix + ".playButton");
	var $pauseButton = $(jqPrefix + ".pauseButton");
	var $stopButton = $(jqPrefix + ".stopButton");
	
	var $volumeSlider = $(jqPrefix + ".volumeSlider");
	var $seekSlider = $(jqPrefix + ".seekSlider");
	
	// disable volume update while dragging
	$volumeSlider.on("slidestart", function() {
		updater.updateVolume = false;
	});
	$volumeSlider.on("slidestop", function() {
		var $input = $(this);
		var percent_value = parseInt($input.val());
		var float_value = percent_value / 100.0;
		$.ajax({
			url: "/volume/" + float_value,
			type: "GET"
		}).success(function(data) {
			var float_value = parseFloat(data);
			var percent_value = Math.round(float_value * 100)
			$volumeSlider.val(percent_value.toString()).slider("refresh");
		}).always(function() {
			updater.updateVolume = true;
		});
	});
	
	// disable position update while dragging
	$seekSlider.on("slidestart", function() {
		updater.updatePosition = false;
	});
	$seekSlider.on("slidestop", function() {
		$input = $(this);
		var value = parseInt($input.val());
		$.ajax({
			url: "/seek/" + value,
			type: "GET"
		}).success(function(data) {
			var value = parseInt(data);
			$seekSlider.val(value);
		}).always(function() {
			updater.updatePositon = true;
		});
	});
	
	var toggleLink = function(link, enabled) {
		if (enabled === true) {
			$(link).removeClass("ui-disabled");
		} else {
			$(link).addClass("ui-disabled");
		}
	}
	
	this.update = function() {
		$.ajax({
			url: "/playerinfo",
			type: "GET",
			dataType: "json"
		}).success(function(data) {
			// disable/enable controls
			if (data.playing === true) {
				$playButton.hide();
				$pauseButton.show();
				toggleLink($stopButton, true);
			} else {
				$playButton.show();
				$pauseButton.hide();
				toggleLink($stopButton, false);
			}
			
			// set volume slider
			if (updater.updateVolume === true) {
				var percentage = Math.round(data.volume * 100);
				$volumeSlider.val(percentage.toString()).slider("refresh");
			}
			
			// set seek slider
			if (updater.updatePosition === true) {
				$seekSlider.attr("max", data.duration).val(data.position).slider("refresh");
			}
		});
	}
}