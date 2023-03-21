function osite(){
    eel.opsite();
  }
  window.addEventListener("resize", function(){
    window.resizeTo(920, 890);
    });

        $('.stat').hide();
        function ca(status,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numclinic,numtrue,namepers,fio,f,i,o,timework,urll,mail,keysl,desc,tupecl,passw,login,numcodcity,numclshot,numn,numpl,shcir,regi,ob,bb,ind){
            if(status=="Определенные сайты"){
                var status = document.getElementById('status').value;
            }
            setTimeout(function() {$('.stat').show();
            setTimeout(function() {$('.stat').hide();
            setTimeout(function() {$('.stat').show();}, (100));
            setTimeout(function() {$('.stat').hide();}, (200));
            setTimeout(function() {$('.stat').show();}, (300));
            setTimeout(function() {$('.stat').hide();}, (400));
          }, (100));
          }, (100));
          valid=true;

          if (numn.length > 10 || numn.includes('+') == true ||numn.length == 9) {
            znumn=document.getElementById('numn').value;
            $("#numn").css({"backgroundColor":"#ffa0a0"});
            document.getElementById('er1').textContent = 'Введите номер верно';
            setTimeout(() => {  
              document.getElementById('er1').textContent = ''; 
              $("#numn").css({"backgroundColor":"white"});
            }, 3000);
            znumn="";
            setTimeout(function() {znumn=numn;}, (150));
            setTimeout(function() {znumn="";}, (300));
            setTimeout(function() {znumn=numn;}, (450));
            setTimeout(function() {znumn="";}, (600));
            setTimeout(function() {znumn=numn;}, (750));
            valid = false;
        }
        if((fio.split(" ").length) - 1 != 2 || (fio.split(" ").length)-1 > 2){
          if(fio != ""){
            fio=document.getElementById('fio').value;
          $("#fio").css({"backgroundColor":"#ffa0a0"});
            document.getElementById('er2').textContent = 'введите ФИО';
            setTimeout(() => {  
              document.getElementById('er2').textContent = '';
              $("#fio").css({"backgroundColor":"white"});
            }, 3000);
            zfio="";
            setTimeout(function() {zfio=fio;}, (150));
            setTimeout(function() {zfio="";}, (300));
            setTimeout(function() {zfio=fio;}, (450));
            setTimeout(function() {zfio="";}, (600));
            setTimeout(function() {zfio=fio;}, (750));
            valid = false;
        }}
        if(mail.includes('@') != true){
          if(mail != ""){
          zmail=document.getElementById('mail').value;
          $("#mail").css({"backgroundColor":"#ffa0a0"});
          document.getElementById('er3').textContent = 'Введите email верно';
          setTimeout(() => {  
          document.getElementById('er3').textContent = ''; 
          $("#mail").css({"backgroundColor":"white"});
        }, 3000);
        zmail="";
            setTimeout(function() {zmail=mail;}, (150));
            setTimeout(function() {zmail="";}, (300));
            setTimeout(function() {zmail=mail;}, (450));
            setTimeout(function() {zmail="";}, (600));
            setTimeout(function() {zmail=mail;}, (750));
        valid = false;
        }}
        
        if(desc.includes("Название") == true){
          if(desc != ""){
            zdesc=document.getElementById('desc').value;
            zdesc="";
          $("#desc").css({"backgroundColor":"#ffa0a0"});
          setTimeout(() => {  $("#desc").css({"backgroundColor":"white"}); }, 3000);
            setTimeout(function() {zdesc=desc;}, (150));
            setTimeout(function() {zdesc="";}, (300));
            setTimeout(function() {zdesc=desc;}, (450));
            setTimeout(function() {zdesc="";}, (600));
            setTimeout(function() {zdesc=desc;}, (750));
            valid = false;
        }}
        
        if(valid == true){
          eel.conti(status,urli,otr1,otr2,urli,notwww,namecl,unamecl,city,cityr,ciadress,street,home,adress,numn,numn,namepers,fio,f,i,o,timework,urll,mail,keysl,desc,tupecl,passw,login,numn,numn,numn,numn,shcir,regi,ob,bb,ind);
        }
        };
          function opr() {
            $('#status').hide();
          }
          function res(valid) {
            document.getElementById('ttt').textContent = 'Введите';
              var namecl = document.getElementById('namecl').value;
              var fio = document.getElementById('fio').value;
              var city = document.getElementById('city').value;
              var numn = document.getElementById('numn').value;
              var cityr = document.getElementById('cityr').value;
              var ciadress = document.getElementById('ciadress').value;
              var timework = document.getElementById('timework').value;
              var street = document.getElementById('street').value;
              var mail = document.getElementById('mail').value;
              var home = document.getElementById('home').value;
              var keysl = document.getElementById('keysl').value;
              var adress = document.getElementById('adress').value;
              var desc = document.getElementById('desc').value;
              var tupecl = document.getElementById('tupecl').value;
              var status = document.getElementById('status').value;
              var passw = document.getElementById('passw').value;
             var urll = document.getElementById('urll').value;
              var otr1 = document.getElementById('otr1').value;
              var otr2 = document.getElementById('otr2').value;
              var notwww = document.getElementById('notwww').value;
              var a=document.getElementById('sta');
              var sta=a.options[a.selectedIndex].text;
              var ind = document.getElementById('ind').value;
              
              if(fio==""){
                fio="Дронов Михаил Иванович";
                f="Дронов";
                i="Михаил";
                o="Иванович";
              }
              if(timework==""){timework="Круглосуточно, ежедневно";}
              if(keysl==""){keysl="нарколог на дом, вывод из запоя, лечение от алкоголизма, кодирование от алкоголизма, наркологическая помощь, лечение наркомании";}
              if(desc==""){desc="Медицинское учреждение, в котором можно получить профессиональную помощь. Правильное лечение освобождает больного от тяжелой разрушающей жизнь патологии. Мы идем в ногу со временем, совмещая богатый опыт и знания в области практической медицины с новейшими методиками диагностики и лечения алкоголизма.";}
              if(passw==""){passw="LW9Tx44d";}
              if(tupecl==""){tupecl="Клиника наркологической помощи";}
              if(valid){
                ca(sta,otr1,otr2,"urli",notwww,namecl,"unamecl",city,cityr,ciadress,street,home,adress,numn,"000","namepers",fio,"f","i","o",timework,urll,mail,keysl,desc,tupecl,passw,"login123",numn,numn,numn,numn," "," "," ","Ф",ind);
            
              }
              else{
                //var divinfo=document.createElement('div');
                /*divinfo.innerHTML="gf";*/
                br="<br>";
                info=document.getElementById('info');
                //info.setAttribute('style','white-space: pre;');
                /*document.getElementById('info').append('Название: '+namecl+br);
                document.getElementById('info').append('ФИО: '+fio+br);*/

                info.innerHTML='<div style="font-weight: 600;display: contents;">Название:</div> '+namecl+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Оф. название:</div> ООО \"'+namecl+'\"'+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Город:</div> '+city+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Область:</div> '+cityr+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Полный адрес:</div> '+ciadress+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Адрес:</div> '+adress+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Улица:</div> '+street+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Дом:</div> '+home+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Индекс:</div> '+ind+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">ФИО:</div> '+fio+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Номер:</div> +7'+numn+br;
                
                
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Время работы:</div> '+timework+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">URL:</div> '+urll+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Пароль:</div> '+passw+br;
                
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Почта:</div> '+mail+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Ключевые слова:</div> '+keysl+br+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Описание:</div> '+desc+br+br;
                info.innerHTML+='<div style="font-weight: 600;display: contents;">Сфера:</div> '+tupecl+br;
                

                /*info.textContent='Название: '+namecl+'\n';
                info.textContent+='\nФИО: '+fio;*/

                /*document.getElementById('info').textContent = 'ФИО: '+fio;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;
                document.getElementById('info').textContent = ': '+namecl;*/
              }
              };
            function getinfo(){
              var namecl = document.getElementById('namecl').value;
              var fio = document.getElementById('fio').value;
              var city = document.getElementById('city').value;
              var numn = document.getElementById('numn').value;
              var cityr = document.getElementById('cityr').value;
              var ciadress = document.getElementById('ciadress').value;
              var timework = document.getElementById('timework').value;
              var street = document.getElementById('street').value;
              var mail = document.getElementById('mail').value;
              var home = document.getElementById('home').value;
              var keysl = document.getElementById('keysl').value;
              var adress = document.getElementById('adress').value;
              var desc = document.getElementById('desc').value;
              var tupecl = document.getElementById('tupecl').value;
              var status = document.getElementById('status').value;
              var passw = document.getElementById('passw').value;
             var urll = document.getElementById('urll').value;
              var otr1 = document.getElementById('otr1').value;
              var otr2 = document.getElementById('otr2').value;
              var notwww = document.getElementById('notwww').value;
              var a=document.getElementById('sta');
              var sta=a.options[a.selectedIndex].text;
              var ind = document.getElementById('ind').value;
              //ca(sta,otr1,otr2,"urli",notwww,namecl,"unamecl",city,cityr,ciadress,street,home,adress,numn,"000","namepers",fio,"f","i","o",timework,urll,mail,keysl,desc,tupecl,passw,"login123",numn,numn,numn,numn," "," "," ","Ф",ind);
              document.getElementById('info').textContent = 'Название: '+namecl;
            }