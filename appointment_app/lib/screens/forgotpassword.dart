import 'package:flutter/material.dart';

import '../widgets/input.dart';
class ForgotPassword extends StatefulWidget {

  @override
  _ForgotPasswordState createState() => _ForgotPasswordState();
}

class _ForgotPasswordState extends State<ForgotPassword> {
  TextEditingController email = TextEditingController();

  forgotPassword(){
    final snackbar = SnackBar(content: Text("If the e-mail is valid, the recovery email will be sent"));
    ScaffoldMessenger.of(context).showSnackBar(snackbar);
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Forgot password"),),
      body: Column(
        children: [
          SizedBox(height: 20,),
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: Input(
                placeholder: "Email",
                onChanged: (value) {},
                controller: email,
                prefixIcon: Icon(Icons.email, size: 20)),
          ),
          SizedBox(height: 20,),
          ElevatedButton(onPressed: (){forgotPassword();}, child: Text("Submit")),

        ],
      ),
    );
  }
}
