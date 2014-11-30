function login(model)
{
  user.isLoggedIn(function(result) {
    log('isLogginedIn '+result);
    if(result)
    {
      user.logout(function(uri) {
        model.logout(uri);
      });
      
      user.isAdmin(function(result) {
        log('isAdmin: '+result);
        model.admin(result);
        
        if(!result)
        {
          user.isMember(function(isMember) {
            if(!isMember)
            {
              window.location="/application";
            }
          });          
        }
      });      
    }
    else
    {
      window.location='/';
    }
  });
}