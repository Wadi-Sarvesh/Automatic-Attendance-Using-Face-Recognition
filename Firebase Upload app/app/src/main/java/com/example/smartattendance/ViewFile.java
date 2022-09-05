package com.example.smartattendance;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class ViewFile extends AppCompatActivity {

    ListView listView;
    DatabaseReference databaseReference;
    List<UploadFile> uploadFiles;
    ArrayAdapter<String> adapter;
    String[] uploads;
    String[] urlList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_file);

        listView = (ListView)findViewById(R.id.listView);
        uploadFiles = new ArrayList<>();

        viewAllFiles();


        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                UploadFile uploadFile = uploadFiles.get(position);
                Intent intent = new Intent(Intent.ACTION_VIEW);
                intent.setData(Uri.parse(uploadFile.getUrl()));
                startActivity(intent);
            }
        });
        registerForContextMenu(listView);

    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);
        if(v.getId() == R.id.listView)
        {
            AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo) menuInfo;
            menu.setHeaderTitle(uploads[info.position]);
            String[] menuItems = getResources().getStringArray(R.array.menu);
            for(int i = 0; i < menuItems.length; i++)
            {
                menu.add(Menu.NONE,i,i,menuItems[i]);

            }
        }
    }

    @Override
    public boolean onContextItemSelected(@NonNull MenuItem item) {
        final AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
        int menuItemIndex = item.getItemId();
        String[] menuItems= getResources().getStringArray(R.array.menu);
        String menuItenmName = menuItems[menuItemIndex];
        Log.d("check menuitemname",menuItenmName);
        DatabaseReference ref = FirebaseDatabase.getInstance().getReference();
        if(menuItenmName.equals("Delete"))
        {Log.d("check menuitemname","Entered if statement");
            Query nameQuery = ref.child("uploads").orderByChild("url").equalTo(urlList[info.position]);
        nameQuery.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String url = null;
                for (DataSnapshot nameSnapshot: dataSnapshot.getChildren()) {

                    url = nameSnapshot.getKey();;
                    nameSnapshot.getRef().removeValue();
                    Intent intent = getIntent();
                    finish();
                    startActivity(intent);
                   


                }
                if(url!= null)
                Log.d("Printing",url);

            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                System.out.println("The read failed: " + databaseError.getCode());
            }
        });}



        Toast.makeText(getApplicationContext(),"Item deleted", Toast.LENGTH_SHORT).show();
        return true;


    }

    private void viewAllFiles() {

        databaseReference = FirebaseDatabase.getInstance().getReference("uploads");
        databaseReference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                for(DataSnapshot postSnapshot: dataSnapshot.getChildren()){
                    UploadFile uploadFile = postSnapshot.getValue(UploadFile.class);
                    uploadFiles.add(uploadFile);
                    Log.d("uploadfiles in override",uploadFiles.toString());
                    uploads = new String[uploadFiles.size()];
                    urlList = new String[uploadFiles.size()];
                    for(int i=0; i<uploads.length;i++){
                        uploads[i] = uploadFiles.get(i).getName();
                        urlList[i] = uploadFiles.get(i).getUrl();
                        adapter = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1,uploads);
                        listView.setAdapter(adapter); }





                }

            }



            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                System.out.println("The read failed: " + databaseError.getCode());
            }
        });


    }
}