import 'package:appointmentapp/screens/forgotpassword.dart';
import 'package:flutter/material.dart';

import 'package:appointmentapp/screens/addDoctor.dart';

// screens

import 'package:appointmentapp/screens/home.dart';

import 'package:appointmentapp/screens/register.dart';
import 'package:appointmentapp/screens/payment.dart';
import 'package:appointmentapp/screens/appointments.dart';

import 'package:appointmentapp/screens/doctor.dart';

import 'package:appointmentapp/screens/login.dart';
import 'package:khalti_flutter/khalti_flutter.dart';
import 'package:khalti_flutter/localization/khalti_localizations.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return KhaltiScope(
        publicKey: "test_public_key_39bbaca1887b46f3a016d3cfd33e7246",
        builder: (context, navigatorKey) {
          return MaterialApp(
              navigatorKey: navigatorKey,
              supportedLocales: const [
                Locale('en', 'US'),
                Locale('ne', 'NP'),
              ],
              localizationsDelegates: const [
                KhaltiLocalizations.delegate,
              ],
              title: 'Doctor Appointment',
              debugShowCheckedModeBanner: false,
              theme: ThemeData(fontFamily: 'Montserrat'),
              initialRoute: '/login',
              routes: <String, WidgetBuilder>{
                "/home": (BuildContext context) => new Home(),
                "/doctor": (BuildContext context) => new Doctor(),
                "/addDoctor": (BuildContext context) => new AddDoctor(),
                "/appointment": (BuildContext context) => new Appointment(),
                "/register": (BuildContext context) => new Register(),
                "/login": (BuildContext context) => new Login(),
                "/payment": (BuildContext context) => new Payment(),
                "/forgot": (BuildContext context) => new ForgotPassword(),
              });
        }
    );
  }
}
