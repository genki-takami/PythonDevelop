import math as m
class cal_disposal_income():
    #コンストラクタ
    def __init__(self, salary):
        self.set_salary(salary)

    #年収を戻り値に
    def get_salary(self):
        return self.__salary

    #年収をセット
    def set_salary(self, salary):
        self.__salary = salary

    #所得　=　給与　−　給与所得控除
    def income(self):
        return self.get_salary() - self.salary_deduction()

    #給与所得控除
    def salary_deduction(self):
        gs = self.get_salary()
        if gs <=1800000:
            if gs < 650000:
                return 650000
            return m.floor(gs * 0.4)
        elif 1800000< gs <=3600000:
            return m.floor(gs * 0.3) + 180000
        elif 3600000< gs <=6600000:
            return m.floor(gs * 0.2) + 540000
        elif 6600000< gs <=10000000:
            return m.floor(gs * 0.1) + 1200000
        elif 10000000 < gs:
            return 2200000

    #課税所得　=　所得　−　所得控除
    def taxable_income(self,supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance):
        return self.income() - self.income_deduction(supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance)

    #所得控除 =　扶養控除　+　配偶者控除　+　障害者控除　+　勤労学生控除　+　社会保険料控除　+　生命保険料控除
    def income_deduction(self,supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance):
        return 380000+self.support_deduction(supported_1,supported_2,supported_3,supported_4)+self.supouse_deduction(supouse_yes_no)+self.handicapped_deduction(your_condition)+self.working_student_deduction(your_status)+self.social_insurance_deduction(your_resident)+self.life_insurance_deduction(life_insurance)

    #扶養控除
    def support_deduction(self,supported_1,supported_2,supported_3,supported_4):
        return supported_1*380000 + supported_2*630000 + supported_3*580000 + supported_4*480000

    #配偶者控除
    def supouse_deduction(self,supouse_yes_no):
        gs = self.get_salary()
        if supouse_yes_no==1:
            if gs<=9000000:
                return 380000
            elif 9000000< gs <=9500000:
                return 260000
            elif 9500000< gs <=10000000:
                return 130000
            else:
                return 0
        else:
            return 0

    #障害者控除
    def handicapped_deduction(self,your_condition):
        if your_condition==1:
            return 270000
        else:
            return 0

    #勤労学生控除
    def working_student_deduction(self,your_status):
        if your_status==1:
            return 270000
        else:
            return 0

    #社会保険料控除
    def social_insurance_deduction(self,your_resident):
        return self.social_insurance(your_resident)

    #生命保険料控除
    def life_insurance_deduction(self,life_insurance):
        if life_insurance<=20000:
            return life_insurance
        elif 20000<life_insurance<=40000:
            return int(life_insurance*0.5+10000)
        elif 40000<life_insurance<=80000:
            return life_insurance*0.25+20000
        elif 80000<life_insurance:
            return 40000
        else:
            return 0

    #納付額　=　課税所得　×　所得税率　−　税額控除
    def tax(self,supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance):
        gs = self.get_salary()
        ti= self.taxable_income(supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance)
        if gs <= 1950000:
            return m.floor(ti * 0.5)
        elif 1950000< gs <=3300000:
            return m.floor(ti * 0.1) - 97500
        elif 3300000< gs <=6950000:
            return m.floor(ti * 0.2) - 427500
        elif 6950000< gs <=9000000:
            return m.floor(ti * 0.23) - 636000
        elif 9000000< gs <=18000000:
            return m.floor(ti * 0.33) - 1536000
        elif 18000000< gs <=40000000:
            return m.floor(ti * 0.4) - 2796000
        elif 40000000 < gs:
            return m.floor(ti * 0.45) - 4796000

    #可処分所得　=　給与　−　納付額　−　社会保険料　−　住民税
    def disposable_income(self,supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance):
        return self.get_salary() - self.tax(supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance) - self.social_insurance(your_resident) - self.resident_tax(your_resident)

    #社会保険料　=　健康保険　+　年金　+　雇用保険
    def social_insurance(self,your_resident):
        return self.health_insurance(your_resident)*12+self.pension()+self.employment_insurance()

    #健康保険
    def health_insurance(self,your_resident):
        gsm = self.get_salary()/12
        if your_resident=="hokkaido":
            return int(gsm*0.1031)
        elif your_resident=="aomori":
            return int(gsm*0.0987)
        elif your_resident=="iwate":
            return int(gsm*0.098)
        elif your_resident=="miyagi":
            return int(gsm*0.101)
        elif your_resident=="akita":
            return int(gsm*0.1014)
        elif your_resident=="yamagata":
            return int(gsm*0.1003)
        elif your_resident=="hukushima":
            return int(gsm*0.0974)
        elif your_resident=="ibaraki":
            return int(gsm*0.0984)
        elif your_resident=="tochigi":
            return int(gsm*0.0992)
        elif your_resident=="gunma":
            return int(gsm*0.0984)
        elif your_resident=="saitama":
            return int(gsm*0.0979)
        elif your_resident=="chiba":
            return int(gsm*0.0981)
        elif your_resident=="tokyo":
            return int(gsm*0.099)
        elif your_resident=="kanagawa":
            return int(gsm*0.0991)
        elif your_resident=="niigata":
            return int(gsm*0.0963)
        elif your_resident=="toyama":
            return int(gsm*0.0971)
        elif your_resident=="ishikawa":
            return int(gsm*0.0999)
        elif your_resident=="hukui":
            return int(gsm*0.0988)
        elif your_resident=="yamanashi":
            return int(gsm*0.099)
        elif your_resident=="nagano":
            return int(gsm*0.0969)
        elif your_resident=="gihu":
            return int(gsm*0.0986)
        elif your_resident=="shizuoka":
            return int(gsm*0.0975)
        elif your_resident=="aichi":
            return int(gsm*0.099)
        elif your_resident=="mie":
            return int(gsm*0.099)
        elif your_resident=="shiga":
            return int(gsm*0.0987)
        elif your_resident=="kyoto":
            return int(gsm*0.1003)
        elif your_resident=="osaka":
            return int(gsm*0.1019)
        elif your_resident=="hyogo":
            return int(gsm*0.1014)
        elif your_resident=="nara":
            return int(gsm*0.1007)
        elif your_resident=="wakayama":
            return int(gsm*0.1015)
        elif your_resident=="tottori":
            return int(gsm*0.10)
        elif your_resident=="shimane":
            return int(gsm*0.1013)
        elif your_resident=="okayama":
            return int(gsm*0.1022)
        elif your_resident=="hiroshima":
            return int(gsm*0.10)
        elif your_resident=="yamaguchi":
            return int(gsm*0.1021)
        elif your_resident=="tokushima":
            return int(gsm*0.103)
        elif your_resident=="kagawa":
            return int(gsm*0.1031)
        elif your_resident=="ehime":
            return int(gsm*0.1002)
        elif your_resident=="kochi":
            return int(gsm*0.1021)
        elif your_resident=="hukuoka":
            return int(gsm*0.1024)
        elif your_resident=="saga":
            return int(gsm*0.1075)
        elif your_resident=="nagasaki":
            return int(gsm*0.1024)
        elif your_resident=="kumamoto":
            return int(gsm*0.1018)
        elif your_resident=="oita":
            return int(gsm*0.1021)
        elif your_resident=="miyazaki":
            return int(gsm*0.1002)
        elif your_resident=="kagoshima":
            return int(gsm*0.1016)
        elif your_resident=="okinawa":
            return int(gsm*0.0995)
        else:
            return 0

    #年金　=　国民年金　+　厚生年金
    def pension(self):
        return 16340*12+self.employees_pension()*12

    #厚生年金
    def employees_pension(self):
        gsm = self.get_salary()/12
        if gsm<93000:
            return 8052
        elif 93000<=gsm<101000:
            return 8967
        elif 101000<=gsm<107000:
            return 9516
        elif 107000<=gsm<114000:
            return 10065
        elif 114000<=gsm<122000:
            return 10797
        elif 122000<=gsm<130000:
            return 11529
        elif 130000<=gsm<138000:
            return 12261
        elif 138000<=gsm<146000:
            return 12993
        elif 146000<=gsm<155000:
            return 13725
        elif 155000<=gsm<165000:
            return 14640
        elif 165000<=gsm<175000:
            return 15555
        elif 175000<=gsm<185000:
            return 16470
        elif 185000<=gsm<195000:
            return 17385
        elif 195000<=gsm<210000:
            return 18300
        elif 210000<=gsm<230000:
            return 20130
        elif 230000<=gsm<250000:
            return 21960
        elif 250000<=gsm<270000:
            return 23790
        elif 270000<=gsm<290000:
            return 25620
        elif 290000<=gsm<310000:
            return 27450
        elif 310000<=gsm<330000:
            return 29280
        elif 330000<=gsm<350000:
            return 31110
        elif 350000<=gsm<370000:
            return 32940
        elif 370000<=gsm<395000:
            return 34770
        elif 395000<=gsm<425000:
            return 37515
        elif 425000<=gsm<455000:
            return 40260
        elif 455000<=gsm<485000:
            return 43005
        elif 485000<=gsm<515000:
            return 45750
        elif 515000<=gsm<545000:
            return 48495
        elif 545000<=gsm<575000:
            return 51240
        elif 575000<=gsm<605000:
            return 53985
        elif 605000<=gsm:
            return 56730

    #雇用保険
    def employment_insurance(self):
        return self.get_salary()*0.003

    #住民税
    def resident_tax(self,your_resident):
        gs = self.get_salary()
        hokkaido=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="hokkaido")
        hokkaido_yubari=dict(pre=1500,ctv=4000,pre_2=gs*0.04,ctv_2=gs*0.065,plus=500+gs*0.005,name="hokkaido_yubari")
        aomori=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="aomori")
        iwate=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="iwate")
        miyagi=dict(pre=2700,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1200,name="miyagi")
        akita=dict(pre=2300,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=800,name="akita")
        yamagata=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="yamagata")
        hukushima=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="hukushima")
        ibaraki=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="ibaraki")
        tochigi=dict(pre=2200,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=700,name="tochigi")
        gunma=dict(pre=2200,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=700,name="gunma")
        saitama=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="saitama")
        chiba=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="chiba")
        tokyo=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="tokyo")
        kanagawa=dict(pre=1800,ctv=3500,pre_2=gs*0.04025,ctv_2=gs*0.06,plus=300+gs*0.00025,name="kanagawa")
        kanagawa_yokohama=dict(pre=1800,ctv=4400,pre_2=gs*0.04025,ctv_2=gs*0.06,plus=300+gs*0.00025+900,name="kanagawa_yokohama")
        niigata=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="niigata")
        toyama=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="toyama")
        ishikawa=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="ishikawa")
        hukui=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="hukui")
        yamanashi=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="yamanashi")
        nagano=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="nagano")
        gihu=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="gihu")
        shizuoka=dict(pre=1900,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=400,name="shizuoka")
        aichi=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="aichi")
        aichi_nagoya=dict(pre=2000,ctv=3300,pre_2=gs*0.04,ctv_2=gs*0.057,plus=500-200,name="aichi_nagoya")
        mie=dict(pre=2500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=1000,name="mie")
        shiga=dict(pre=2300,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=800,name="shiga")
        kyoto=dict(pre=2100,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=600,name="kyoto")
        osaka=dict(pre=1800,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=300,name="osaka")
        hyogo=dict(pre=2300,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=800,name="hyogo")
        hyogo_toyooka=dict(pre=2300,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.061,plus=800+gs*0.001,name="hyogo_toyooka")
        nara=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="nara")
        wakayama=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="wakayama")
        tottori=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="tottori")
        shimane=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="shimane")
        okayama=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="okayama")
        hiroshima=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="hiroshima")
        yamaguchi=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="yamaguchi")
        tokushima=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="tokushima")
        kagawa=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="kagawa")
        ehime=dict(pre=2200,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=700,name="ehime")
        kouchi=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="kouchi")
        hukuoka=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="hukuoka")
        saga=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="saga")
        nagasaki=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="nagasaki")
        kumamoto=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="kumamoto")
        oita=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="oita")
        miyazaki=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="miyazaki")
        kagoshima=dict(pre=2000,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=500,name="kagoshima")
        okinawa=dict(pre=1500,ctv=3500,pre_2=gs*0.04,ctv_2=gs*0.06,plus=0,name="okinawa")
        #配列
        prefectures=[hokkaido,aomori,iwate,miyagi,akita,yamagata,hukushima,ibaraki,tochigi,
        gunma,saitama,chiba,tokyo,kanagawa,niigata,toyama,ishikawa,hukui,yamanashi,nagano,gihu,
        shizuoka,aichi,mie,shiga,kyoto,osaka,hyogo,nara,wakayama,tottori,shimane,okayama,hiroshima,
        yamaguchi,tokushima,kagawa,ehime,kouchi,hukuoka,saga,nagasaki,kumamoto,oita,miyazaki,kagoshima,okinawa]

        for i in prefectures:
            if your_resident==i["name"]:
                return i["pre"]+i["ctv"]+i["pre_2"]+i["ctv_2"]+i["plus"]
            else:
                continue
