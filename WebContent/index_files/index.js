$( document ).ready(function() {
	var isLoad = true;
    console.log( "ready!" );
    jQuery("#taskGrid").jqGrid({
        datatype: 'local',
//    	url:"http://127.0.0.1:8080/tasks",
//    	datatype: "json",
        colNames:['Importance','Assignor', 'Assignee','Category', 'Title','Time','Deadline'],
        colModel:[
          {name:'Importance',index:'Importance', width:100},
          {name:'Assignor',index:'Assignor', width:100,editable:true,edittype:"select",editoptions:{value:"Me:Me;All subordinates:All subordinates;I:I;Boss:Boss;Client A:Client A;Client B:Client B;Father:Father;HR:HR;Subordinate C:Subordinate C;Wife:Wife;Yamamoto-san:Yamamoto-san;CEO:CEO;PR:PR;Mr.X:Mr.X;General affairs:General affairs;Takahashi-san:Takahashi-san"}},
          {name:'Assignee',index:'Assignee', width:150,editable:true,edittype:"select",editoptions:{value:"Me:Me;Yoko-san:Yoko-san;Subordinate A:Subordinate A;Subordinate B:Subordinate B;Subordinate C:Subordinate C;Subordinate D:Subordinate D;Boss:Boss;All subordinate:All subordinate;Takashi-san:Takashi-san;Watanabe-san:Watanabe-san;I:I;Subordinate E:Subordinate E"}},
          {name:'Category',index:'Category', width:100, align:"right",editable: true,edittype:"select",editoptions:{value:"Both:Both;Private:Private;Job:Job"}},   
          {name:'Title',index:'Title', width:450,sortable:false,editable:true,editoptions:{size:25}},
          {name:'Time',index:'Time', width:100,align:"right",editable:true,editoptions:{size:25}},    
          {name:'Deadline',index:'Category', width:150, sorttype:"date",editable:true,editoptions:{size:25}}   
        ],
        rowNum:30,
        rowList:[20,30,50],
        pager: '#pagered',
        loadonce: false,
        height: 500,
        sortname: 'id',
        viewrecords: true,
        loadComplete : function () {
        	console.log("load Complete.");
        	if (isLoad) {
        		getData();
        		isLoad=false;
            	jQuery("#cData").trigger('click');
			}
        },
//        gridComplete : function () {
//        	console.log("before send.");
//        	if (isLoad) {
//        		getData();
//        		isLoad=false;
//			}
//        },
        sortorder: "desc",
        caption:"Task List",
        editurl:"http://localhost:8888/task/add"
    });
    $("#bedata").click(function(){
    	isLoad=true;
    	setTimeout(function(){
    		jQuery("#Deadline").val('06/26 Mon. 20:00');
    	},500);
    	jQuery("#taskGrid").jqGrid('editGridRow',"new",{height:280,reloadAfterSubmit:true});
    });
//    var mydata = [
//          {"Importance":"1","Assignor":"Me","Assignee":"Subordinate AB",Category:"Job",Assignee:"good Assignee",Time:"10",Deadline:"2007-09-01"}
//        ];
//    var mydata = [
//    	{"Importance":"Low","Assignor":"Me","Assignee":"Boss",Category:"Job",Title:"Request to check the presentation for Project A",Time:"15",Deadline:"06/26 Mon. 17:00"},
//    	{"Importance":"Mid","Assignor":"HR","Assignee":"Me",Category:"Job",Title:"Check the resume of the engineer candidate A and answer",Time:"20",Deadline:"06/26 Mon. 20:00"},
//    	{"Importance":"Low","Assignor":"Takahashi-san","Assignee":"Subordinate A",Category:"Job",Title:"Instruct to change the date of the meeting about Client C",Time:"5",Deadline:"06/26 Mon. 20:00"},
//    	{"Importance":"High","Assignor":"Client A","Assignee":"Me",Category:"Job",Title:"Make the report about spec. out about product B",Time:"180",Deadline:"06/27 Tue. 09:00"},
//    	{"Importance":"High","Assignor":"Client A","Assignee":"Subordinate A",Category:"Job",Title:"Instruct to print the deck for the appointment with Client A",Time:"5",Deadline:"06/27 Tue. 15:00"},
//    	{"Importance":"Mid","Assignor":"Client B","Assignee":"Me",Category:"Job",Title:"Confirm the drawing of product AA",Time:"120",Deadline:"06/27 Tue. 18:00"},
//    	{"Importance":"High","Assignor":"All subordinates","Assignee":"Me",Category:"Job",Title:"Feedback about the meeting with Client C",Time:"30",Deadline:"06/27 Tue. 20:00"},
//    	{"Importance":"Mid","Assignor":"Me","Assignee":"Takashi-san",Category:"Job",Title:"Fix the problem of the VPN connection",Time:"15",Deadline:"06/27 Tue. 20:00"},
//    	{"Importance":"Mid","Assignor":"All subordinates","Assignee":"Yoko-san",Category:"Job",Title:"Instruct to arrange the term-end drinking of the division",Time:"10",Deadline:"06/27 Tue. 20:00"},
//    	{"Importance":"Mid","Assignor":"Client B","Assignee":"Me",Category:"Job",Title:"Set the meeting about Client B with Subordinate A",Time:"5",Deadline:"06/27 Tue. 20:00"},
//    	{"Importance":"Mid","Assignor":"Client B","Assignee":"Me",Category:"Job",Title:"Confirm the drawing of product YY",Time:"120",Deadline:"06/28 Wed. 12:00"},
//    	{"Importance":"Mid","Assignor":"Me","Assignee":"Subordinate B",Category:"Job",Title:"Make the agenda for the next meeting with client B",Time:"60",Deadline:"06/28 Wed. 12:00"},
//    	{"Importance":"Mid","Assignor":"Me","Assignee":"Me",Category:"Job",Title:"Prepare a GPU instance for the image recognition",Time:"60",Deadline:"06/28 Wed. 12:00"},
//    	{"Importance":"Mid","Assignor":"Boss","Assignee":"Me",Category:"Job",Title:"Refer the specification of component C",Time:"30",Deadline:"06/28 Wed. 12:00"},
//    	{"Importance":"High","Assignor":"Boss","Assignee":"Me",Category:"Job",Title:"Create the deck for the monthly meeting",Time:"30",Deadline:"06/28 Wed. 15:00"},
//    	{"Importance":"Low","Assignor":"Subordinate C","Assignee":"Me",Category:"Job",Title:"Confirm the drawing of product DD",Time:"90",Deadline:"06/28 Wed. 18:00"},
//    	{"Importance":"Mid",'Assignor':"Me","Assignee":"Subordinate B",Category:"Job",Title:"Have a design review about Product BB",Time:"90",Deadline:"06/29 Fri. 12:00"}
//    	];
    var mydata
    function getData() {
    	$.ajax({
    		url : 'http://127.0.0.1:8080/tasks',
    		type : "GET",
    		dataType : 'json', // 追加
    		success : function(res) {
    			mydata = res.tasks;
    			console.log(mydata);
    			$("#taskGrid")[0].addJSONData(mydata);
    		    jQuery("#taskGrid").jqGrid('setGridParam',{ 
//    		    	datatype: 'local',
    		    	sortname:'Importance',
    		    	sortorder: 'asc',
    		    	data:mydata
    		    	}).trigger("reloadGrid");
    		}
    	});
    }
//    getData();
});

