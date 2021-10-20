/*
* 表单校验：用户名/密码不为空、两次密码一致、用户名不能超过15字符
* */

function username_check() {
	let username =  document.getElementById("username").value;
	let username_hint = document.getElementById("username_hint");
	if (username === '') {
		username_hint.innerHTML = "用户名不能为空";
		return false;
	} else if (username.length > 15) {
		username_hint.innerHTML = "用户名不能超过15个字符";
		return false;
	} else {
		username_hint.innerHTML = "";
		return true;
	}
}

function password1_check() {
	let password1 = document.getElementById("password1").value;
	let password1_hint = document.getElementById("password1_hint");
	if (password1 === '') {
		password1_hint.innerHTML = "密码不能为空";
		return false;
	} else {
		password1_hint.innerHTML = "";
		return true;
	}
}

function password2_check() {
	let password1 = document.getElementById("password1").value;
	let password2 = document.getElementById("password2").value;
	let password2_hint = document.getElementById("password2_hint");
	if(password2 !== password1) {
		password2_hint.innerHTML = "两次密码不一致";
		return false;
	} else {
		password2_hint.innerHTML = "";
		return true;
	}
}

/*
* 阻止表单提交 提示会存在短路
*/
function submit_check(s) {
	if (s === 'register')
	    return username_check() && password1_check() && password2_check()
	else if (s==='login')
		return username_check() && password1_check()
}

/**
 * 取消提示
 */
function tips_cancel() {
	let tips = document.getElementById("tips");
	tips.innerHTML = "";
}

