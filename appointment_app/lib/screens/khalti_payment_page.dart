import 'package:flutter/material.dart';
import 'package:khalti_flutter/khalti_flutter.dart';

import 'addAppointment.dart';

class KhaltiPaymentPage extends StatefulWidget {

  String id;
  KhaltiPaymentPage ({
  this.id
});
  @override
  State<KhaltiPaymentPage> createState() => _KhaltiPaymentPageState();
}

class _KhaltiPaymentPageState extends State<KhaltiPaymentPage> {
  TextEditingController amountController = TextEditingController();

  getAmt() {
    return int.parse(amountController.text) * 100; // Converting to paisa
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromRGBO(88, 124, 202,1.0),
        title: const Text('Khalti Pay'),
      ),
      body: Container(
        padding: const EdgeInsets.all(15),
        child: ListView(
          children: [
            const SizedBox(height: 15),
            // For Amount
            TextField(
              controller: amountController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                  labelText: "Enter Amount to pay",
                  enabledBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.black),
                    borderRadius: BorderRadius.all(Radius.circular(8)),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.green),
                    borderRadius: BorderRadius.all(Radius.circular(8)),
                  )),
            ),
            const SizedBox(
              height: 8,
            ),
            // For Button
            MaterialButton(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8),
                    side: const BorderSide(color: Colors.red)),
                height: 50,
                color: Color.fromRGBO(88, 124, 202,1.0),
                child: const Text(
                  'Pay With Khalti',
                  style: TextStyle(color: Colors.white, fontSize: 22),
                ),
                onPressed: () {
                  KhaltiScope.of(context).pay(
                    config: PaymentConfig(
                      amount: getAmt(),
                      productIdentity: 'test',
                      productName: 'VHC',
                    ),
                    preferences: [
                      PaymentPreference.khalti,
                      PaymentPreference.connectIPS,
                      PaymentPreference.mobileBanking,
                    ],
                    onSuccess: (su) {
                      const successsnackBar = SnackBar(
                        content: Text('Payment Successful'),
                        backgroundColor: Colors.greenAccent,
                      );
                      ScaffoldMessenger.of(context)
                          .showSnackBar(successsnackBar);
                      Navigator.of(context)
                          .push(new MaterialPageRoute(
                        builder: (BuildContext context) =>
                            new AddAppointment(
                                index: widget.id),
                      ));
                    },
                    onFailure: (fa) {
                      const failedsnackBar = SnackBar(
                        content: Text('Payment Failed'),
                        backgroundColor: Colors.redAccent,
                      );
                      ScaffoldMessenger.of(context)
                          .showSnackBar(failedsnackBar);
                    },
                    onCancel: () {
                      const cancelsnackBar = SnackBar(
                        content: Text('Payment Cancelled'),
                        backgroundColor: Colors.redAccent,
                      );
                      ScaffoldMessenger.of(context)
                          .showSnackBar(cancelsnackBar);
                    },
                  );
                }),
          ],
        ),
      ),
    );
  }
}
