SELECT wx.Id
FROM Weather wx, Weather wy
WHERE dateDiff(wx.recordDate, wy.recordDate) = 1 AND wx.Temperature > wy.Temperature