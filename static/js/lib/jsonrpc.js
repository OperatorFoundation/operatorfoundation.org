lastid=0;

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
  isMember: function(callback)
  {
    jsonrpcCallback('/api/user', 'isMember', [], callback);
  },
  login: function(callback)
  {
    jsonrpcCallback('/api/user', 'login', [], callback);
  },
  logout: function(callback)
  {
    jsonrpcCallback('/api/user', 'logout', [], callback);
  },
  apply: function(username, application)
  {
    jsonrpc('/api/user', 'apply', [username, application]);
  },
  hasApplied: function(callback)
  {
    jsonrpcCallback('/api/user', 'hasApplied', [], callback);
  }
};

salon={
  add: function(name, displayName)
  {
    jsonrpc('/api/salon', 'add', [name, displayName]);
  },
  delete: function(name)
  {
    jsonrpc('/api/salon', 'delete', [name]);
  },
  list: function(callback)
  {
    jsonrpcCallback('/api/salon', 'list', [], callback);
  },
  getDisplayName: function(name, callback)
  {
    jsonrpcCallback('/api/salon', 'getDisplayName', [name], callback);    
  },
  getThreads: function(name, callback)
  {
    jsonrpcCallback('/api/salon', 'getThreads', [name], callback);        
  }
};

post={
  get: function(msgid, callback)
  {
    jsonrpcCallback('/api/post', 'get', [msgid], callback);
  }  
};

draft={
  add: function(salon, subject, body, replyto, draft, callback)
  {
    jsonrpcCallback('/api/draft', 'add', [salon, subject, body, replyto, draft], callback);
  },
  list: function(callback)
  {
    jsonrpcCallback('/api/draft', 'list', [], callback)
  },
  get: function(msgid, callback)
  {
    jsonrpcCallback('/api/draft', 'get', [msgid], callback);
  },
  remove: function(msgid, callback)
  {
    jsonrpcCallback('/api/draft', 'remove', [msgid], callback);
  },
  save: function(msgid, subject, body, postit)
  {
    jsonrpc('/api/draft', 'save', [msgid, subject, body, postit]);
  }
};

item={
  inventory: function(callback)
  {
    jsonrpcCallback('/api/item', 'inventory', [], callback)
  }
};

todo={
  add: function(text, callback)
  {
    jsonrpcCallback('/api/todo', 'add', [text], callback);
  },
  list: function(callback)
  {
    jsonrpcCallback('/api/todo', 'list', [], callback)
  }
}