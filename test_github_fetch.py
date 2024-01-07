import pytest
import github_fetch

def test_github_fetch_api():
    
    actual_user = github_fetch.get_github_user('karpathy')
    expected_user = {
        
    }
    expected_user.update({
        'login':'karpathy',
        'html_url':'https://github.com/karpathy',
        'url':"https://api.github.com/users/karpathy",
        "followers":59731,
        'following':7
    })
    
    assert actual_user['url']==expected_user['url'],"url doesn't match "
    assert actual_user['login']==expected_user['login'],"login doesn't match "
    assert actual_user['html_url']==expected_user['html_url'],f"html url doesn't match{actual_user['html_url']}"
    assert actual_user['followers']==expected_user['followers'],"followers doesn't match"
    assert actual_user['following']==expected_user['following'],"following match"