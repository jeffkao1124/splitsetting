function initializeApp(data) {  //初始化LIFF
  var userid = data.context.userId; //取得ID
}

function pushMsg(item, cost, payer) {
  if (item == '' || cost == '' || payer == '') {  //資料檢查
  alert('每個項目都必須輸入！');
  return;
  }
  var msg = "分帳 ";  //回傳訊息字串
  msg = msg + item + " ";
  msg = msg + cost + " ";
  msg = msg + payer ;

/*
  var i=0;
  do {
  msg = msg + splitter;
　i++;
  }while(i<10);

  var msg = "分帳 ";  //回傳訊息字串
  msg = msg + item + " ";
  msg = msg + cost + " ";
  msg = msg + payer + " ";
  msg = msg + splitter;*/

  liff.sendMessages([  //推播訊息
    { type: 'text',
      text: msg 
    },
  ])
    .then(() => {
      liff.closeWindow();  //關閉視窗
    });
}

$(document).ready(function () {
  liff.init(function (data) {  //初始化LIFF
    initializeApp(data);
  });
  
  $('#sure').click(function (e) {  //按下確定鈕
    pushMsg($('#item').val(), $('#cost').val(), $('#payer').val());
  });
});

