package com.razor.mobileware;

import android.os.Bundle;
import android.app.Activity;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

import org.json.JSONObject;
import org.json.JSONException;

public class RzMobileWare extends Activity {

    private String acctId = "123-joe-8a35c518";

    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        Button login = (Button) findViewById(R.id.btn_login);
        //  add login click listener
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Editable user_id = ((EditText)findViewById(R.id.et_user)).getText();
                Editable password = ((EditText)findViewById(R.id.et_password)).getText();

                JSONObject cred = new JSONObject();
                try {
                    cred.put("user_id",user_id.toString());
                    cred.put("password", password.toString());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                //  send request(json.data) to rz
                URL url = null;
                try {
                    url = new URL("http://localhost:8000/razorcrm/rzm_login");
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }

                HttpURLConnection connection = null;
                if (url != null) {
                    try {
                        connection = (HttpURLConnection)url.openConnection();
                        connection.setDoOutput(true);
                        connection.setDoInput(true);
                        connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
                        connection.setRequestProperty("Accept", "application/json");
                        connection.setRequestMethod("POST");

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }

                if (connection != null) {
                    try {
                        OutputStreamWriter wr = new OutputStreamWriter(connection.getOutputStream());
                        wr.write(cred.toString());
                        wr.flush();

                        StringBuilder sb = new StringBuilder();
                        int httpCode = connection.getResponseCode();
                        if (httpCode == HttpURLConnection.HTTP_OK) {
                            BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(),"utf-8"));
                            String line = null;

                            while ((line = br.readLine()) != null) {
                                sb.append(line).append("\n");
                            }

                            br.close();

                            System.out.println(""+sb.toString());

                        }else{
                            System.out.println(connection.getResponseMessage());
                        }

                    } catch (IOException e) {
                        System.out.println(e.getMessage());
                        System.out.println();

                        for (StackTraceElement stkTrace : e.getStackTrace()) {
                            System.out.println(stkTrace.toString());
                        }

                    }

                }
            }
        });
    }
}
