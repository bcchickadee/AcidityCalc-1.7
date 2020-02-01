#AcidityCalc stable build 1.7 (Feb 01 2020)
#AcidityCalc 안정 빌드 1.7 (2020년 2월 1일)
#This program calculates various properties (e. g.: pH, acidity, Hydrogen Ion Concentration ([H+])) regarding acidic properties, based on user data input of solution properties.
#이 프로그램은 입력 데이터를 통해 pH, 수소 이온 몰농도 등 용액의 여러 화학적 특성을 수치적으로 계산합니다.


#The math module is required for calculating logs and exponents.
#로그와 지수 계산을 위해 math 모듈이 필요합니다.
import math

#This section is for the user interface and redirection functions (initial program sequence).
#이 섹션은 유저 인터페이스와 리디렉션 함수 (초기 프로그램 시퀀스)를 정의합니다.
def InitialScreen(KeyInput):
    if int(KeyInput)==1:
        print('1번 기능: 수소 이온 몰농도([H+])를 입력하여 pH를 산출합니다.')
        HydrogenIonConcentration=input('\n수소 이온 몰농도를 입력해 주십시오. 단위: mol/ℓ\n')
        print('[H+]='+HydrogenIonConcentration+' 인 용액의 pH는:')
        HydrogenIonConcentration_to_pH(HydrogenIonConcentration)
        print('입니다.')
        print('=================================\n\n')
        #1st Option: Calculates pH based on user input of Hydrogen Ion Molar Concentration ([H+])
        #제 1번 기능: 수소 이온 몰농도 ([H+])를 입력하여 산성도 (pH)를 산출
    elif int(KeyInput) ==2:
        print('2번 기능: pH를 입력하여 수소 이온 몰농도([H+])를 산출합니다.')
        pH=input('\npH를 입력하여 주십시오.\n')
        print('pH='+pH+' 인 용액의 수소 이온 몰농도 ([H+])는:')
        pH_to_HydrogenIonConcentration(pH)
        print('mol/ℓ 입니다.')
        print('=================================\n\n')
        #2nd Option: Calculates Hydrogen Ion Molar Concentration ([H+]) based on user input of pH
        #제 2번 기능: 산성도 (pH)를 입력하여 수소 이온 몰농도([H+])를 산출
    elif int(KeyInput) ==3:
        print('3번 기능: pH와 용액 부피를 입력하여 수소 이온 몰수를 산출합니다.')
        pH=input('\npH를 입력하여 주십시오.\n')
        SolutionVolume=input('\n용액의 부피를 입력하여 주십시오. 단위: 리터(ℓ)\n')
        print('pH='+pH+' 이고 부피가 '+SolutionVolume+'ℓ인 용액의 수소 이온 몰수는:')
        pH_Volume_to_HydrogenIonMol(pH, SolutionVolume)
        print('mol입니다.')
        print('=================================\n\n')
        #3rd Option: Calculates number of mols of Hydrogen Ions based on user input of pH and Solution Volume
        #제 3번 기능: 산성도 (pH)와 용액 부피를 입력하여 수소 이온 몰수를 산출
    elif int(KeyInput) ==4:
        print('4번 기능: 수소 이온 몰농도([H+])와 용액 부피를 입력하여 수소 이온 몰수를 산출합니다.')
        HydrogenIonConcentration=input('\n수소 이온 몰농도를 입력해 주십시오. 단위: mol/ℓ\n')
        SolutionVolume=input('\n용액의 부피를 입력하여 주십시오. 단위: 리터(ℓ)\n')
        print('수소 이온 몰농도([H+])가 '+HydrogenIonConcentration+'이고 용액의 부피가 '+SolutionVolume+'인 용액의 수소 이온 몰수는:')
        HydrogenIonConcentration_Volume_to_HydrogenIonMol(HydrogenIonConcentration, SolutionVolume)
        print('mol입니다.')
        print('=================================\n\n')
        #4th Option: Calculates number of mols of Hydrogen Ions based on user input of Hydrogen Ion Molar Concentration and Solution Volume
        #제 4번 기능: 수소 이온 몰농도([H+])와 용액 부피를 입력하여 수소 이온 몰수를 산출
    elif int(KeyInput) ==5:
        print('5번 기능: 산성도 (pH)를 입력하여 액성을 판별합니다.')
        pH=input('\npH를 입력하여 주십시오.\n')
        print('용액의 액성은:')
        pH_to_Acidity(pH)
        print('입니다.')
        print('=================================\n\n')
        #5th Option: Displays Acidity based on user input of pH
        #제 5번 기능: 산성도 (pH)를 입력하여 액성을 판별
    elif int(KeyInput) ==6:
        print('6번 기능: 수소 이온 몰농도 ([H+])를 입력하여 액성을 판별합니다.')
        HydrogenIonConcentration=input('\n수소 이온 몰농도를 입력해 주십시오. 단위: mol/ℓ\n')
        print('용액의 액성은:')
        HydrogenIonConcentration_to_Acidity(HydrogenIonConcentration)
        print('입니다.')
        print('=================================\n\n')
        #6th Option: Displays Acidity based on user input of Hydrogen Ion Molar Concentration
        #제 6번 기능: 수소 이온 몰농도 ([H+])를 입력하여 액성을 판별
    elif int(KeyInput)==7:
        UserPreference=input('정말로 프로그램을 종료하시겠습니까? (y/n)\n')
        return QuittingSequence(UserPreference)
        #7th Option: Exits the program
        #제 7번 기능: 프로그램 종료
    else:
        print('에러: 올바른 선택지를 입력하십시오.')
        #Invalid Option: Displays Error Message
        #유효하지 않은 기능: 에러 메시지 표시


#This section is for the definitions for all of the functions required to display the values in this program.
#이 섹션은 프로그램에서 요구하는 기능의 결과값을 도출하기 위한 함수의 정의를 나열합니다.

def HydrogenIonConcentration_to_pH(HydrogenIonConcentration):
    print(-math.log10(float(HydrogenIonConcentration)))
    #HydrogenIonConcentration_to_pH function definition for 1st option
    #제 1번 기능에 대한 HydrogenIonConcentration_to_pH 함수 정의

def pH_to_HydrogenIonConcentration(pH):
    print(0.1**(float(pH)))
    #pH_to_HydrogenIonConcentration function definition for 2nd option
    #제 2번 기능에 대한 pH_to_HydrogenIonConcentration 함수 정의

def pH_Volume_to_HydrogenIonMol(pH, SolutionVolume):
    print((0.1**(float(pH)))*float(SolutionVolume))
    #pH_Volume_to_HydrogenIonMol function definition for 3rd option
    #제 3번 기능에 대한 pH_Volume_to_HydrogenIonMol 함수 정의

def HydrogenIonConcentration_Volume_to_HydrogenIonMol(HydrogenIonConcentration, SolutionVolume):
    print(float(HydrogenIonConcentration)*float(SolutionVolume))
    #HydrogenIonConcentration_Volume_to_HydrogenIonMol function definition for 4th option
    #제 4번 기능에 대한 HydrogenIonConcentration_Volume_to_HydrogenIonMol 함수 정의

def pH_to_Acidity(pH):
    if float(pH)<7:
        print('산성')
    if float(pH)==7:
        print('중성')
    if float(pH)>7:
        print('염기성')
    #pH_to_Acidity function definition for 5th option
    #제 5번 기능에 대한 pH_to_Acidity 함수 정의
    #Developer Note: Equilibrium constant differences based on external conditions such as temperature, pressure etc. are currently not supported in this build. The set value is set for 25ºC, 1atm.
    #개발자 노트: 현재 빌드에서는 온도, 압력 등 외부 조건에 따른 이온화 상수 변화는 지원하지 않습니다. 외부 조건은 25ºC, 1atm으로 고정되어 있습니다.

def HydrogenIonConcentration_to_Acidity(HydrogenIonConcentration):
    if float(HydrogenIonConcentration)>0.1**7:
        print('산성')
    if float(HydrogenIonConcentration)==0.1**7:
        print('중성')
    if float(HydrogenIonConcentration)<0.1**7:
        print('염기성')
    #HydrogenIonConcentration_to_Acidity function definition for 6th option
    #제 6번 기능에 대한 HydrogenIonConcentration_to_Acidity 함수 정의
    #Developer Note: Equilibrium constant differences based on external conditions such as temperature, pressure etc. are currently not supported in this build. The set value is set for 25ºC, 1atm.
    #개발자 노트: 현재 빌드에서는 온도, 압력 등 외부 조건에 따른 이온화 상수 변화는 지원하지 않습니다. 외부 조건은 25ºC, 1atm으로 고정되어 있습니다.

def QuittingSequence(UserPreference):
    if str(UserPreference)=="y":
        quit()
    elif str(UserPreference)=="n":
        print('프로그램 종료를 취소하였습니다.\n프로그램을 다시 시작합니다.\n\n')
    else:
        print('에러: 올바른 선택지를 입력하십시오.\n\n')
        return InitialScreen(7)
    #QuittingSequence function definition for 7th option
    #제 7번 기능에 대한 QuittingSequence 함수 정의

#This section consists of the main sequence when initiating the program.
#이 섹션은 프로그램 실행 시 사용되는 주요 시퀀스입니다.

print('AcidityCalc build 1.7')
print('Release Feb 01 2020')
print('Development by bcchickadee\n\n')
print('프로그램 설명')
print('=================================')
print('이 프로그램은 입력 데이터를 통해 pH, 수소 이온 몰농도 등 용액의 여러 화학적 특성을 수치적으로 계산해주는 프로그램입니다.\n\n')
#Program Description at initial startup - this message is only displayed once.
#초기 시작 화면의 프로그램 설명 - 이 메시지는 한 번만 표시됩니다.
    
while True:
    print('실행할 기능을 입력해 주십시오.\n')
    print('1: 수소 이온 몰농도([H+])로 pH를 계산')
    print('2: pH로 수소 이온 몰농도([H+]) 계산')
    print('3: pH와 부피로 수소 이온 몰수 계산')
    print('4: 수소 이온 몰농도([H+])와 부피로 수소 이온 몰수 계산')
    print('5: pH로 액성 판단')
    print('6: 수소 이온 몰농도로 액성 판단')
    print('7. 프로그램 종료\n')
    #Listing of functions for the user to select
    #사용자 선택을 위한 함수 나열
    KeyInput=input('실행 기능: ')
    print('=================================\n')
    InitialScreen(KeyInput)
