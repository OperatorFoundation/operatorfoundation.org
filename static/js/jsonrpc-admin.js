function jsonrpc(url, methodName, params)
{
  var id=lastid;
  lastid=lastid+1;

  var data=JSON.stringify({'method': methodName, 'params': params, 'id': id});
  $.post(url, data);
}

function wrap(callback)
{
  if(callback!=null)
  {
    return function(data) {callback(data.result);};
  }
  else
  {
    return function(data) {};
  }
}

function jsonrpcCallback(url, methodName, params, callback)
{
  var id=lastid;
  lastid=lastid+1;

  var data=JSON.stringify({'method': methodName, 'params': params, 'id': id});
  $.post(url, data, wrap(callback));
}

user={
  isLoggedIn: function(callback)
  {
    jsonrpcCallback('/api/user', 'isLoggedIn', [], callback);
  },
  isAdmin: function(callback)
  {
    jsonrpcCallback('/api/user', 'isAdmin', [], callback);
  },
  login: function(callback)
  {
    jsonrpcCallback('/api/user', 'login', [], callback);
  },
  logout: function(callback)
  {
    jsonrpcCallback('/api/user', 'logout', [], callback);
  }
};
