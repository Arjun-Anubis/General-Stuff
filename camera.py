import uiautomation as auto



handle = auto.ButtonControl(automation_id="video-button", searchDepth = 20)

handle.getInvokePattern().Invoke()
