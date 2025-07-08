#!/usr/bin/env python3
"""
التحقق من إضافة الطلاب الجدد
Verify the addition of new students
"""

import os
import sys
import django

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alhassan.settings')
django.setup()

from competitions.models import Participant

def verify_new_students():
    """التحقق من الطلاب الجدد المضافين"""
    
    print("🔍 التحقق من الطلاب الجدد المضافين...")
    print("=" * 60)
    
    # البحث عن الطلاب المضافين
    students_to_verify = [
        'فاطمة الزهراء باعسري',
        'عمران بلقاري'
    ]
    
    found_students = []
    missing_students = []
    
    for student_name in students_to_verify:
        student = Participant.objects.filter(name=student_name).first()
        
        if student:
            found_students.append(student)
            print(f"✅ تم العثور على الطالب: {student.name}")
            print(f"   📚 المستوى: {student.get_grade_display()}")
            print(f"   👥 الفوج: {student.get_group_display()}")
            print(f"   🆔 المعرف: {student.id}")
            print(f"   📅 تاريخ الإضافة: {student.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print()
        else:
            missing_students.append(student_name)
            print(f"❌ لم يتم العثور على الطالب: {student_name}")
            print()
    
    print("=" * 60)
    print("📊 نتائج التحقق:")
    print(f"✅ تم العثور على {len(found_students)} طالب/طالبة")
    print(f"❌ لم يتم العثور على {len(missing_students)} طالب/طالبة")
    
    return found_students, missing_students

def show_grade_8_group_1_students():
    """عرض جميع طلاب المستوى الثاني إعدادي - الفوج الأول"""
    
    print("\n" + "=" * 60)
    print("📋 جميع طلاب المستوى الثاني إعدادي - الفوج الأول")
    print("=" * 60)
    
    students = Participant.objects.filter(
        grade=8,  # المستوى الثاني إعدادي
        group=1   # الفوج الأول
    ).order_by('name')
    
    if students.exists():
        print(f"📊 العدد الإجمالي: {students.count()} طالب/طالبة")
        print()
        
        for i, student in enumerate(students, 1):
            print(f"{i:2d}. {student.name}")
            print(f"    🆔 المعرف: {student.id}")
            print(f"    📅 تاريخ الإضافة: {student.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()
    else:
        print("❌ لا يوجد طلاب في هذا المستوى والفوج")
    
    return students

def generate_student_access_info():
    """إنشاء معلومات الوصول للطلاب"""
    
    print("\n" + "=" * 60)
    print("🔗 معلومات الوصول للطلاب الجدد")
    print("=" * 60)
    
    print("🌐 رابط دخول الطلاب:")
    print("   http://192.168.1.156:8000/student/login/")
    print()
    print("🔑 رمز الدخول:")
    print("   ben25")
    print()
    print("📋 خطوات الدخول للطلاب:")
    print("   1. افتح المتصفح واذهب إلى الرابط أعلاه")
    print("   2. أدخل رمز الدخول: ben25")
    print("   3. أدخل اسمك الكامل كما هو مسجل في النظام")
    print("   4. اختر المستوى الدراسي: الثاني إعدادي")
    print("   5. اختر مستوى الصعوبة المناسب")
    print("   6. ابدأ في حل المسابقات")
    print()
    
    # عرض الأسماء المسجلة
    students = Participant.objects.filter(grade=8, group=1).order_by('name')
    if students.exists():
        print("📝 الأسماء المسجلة في النظام:")
        for student in students:
            print(f"   • {student.name}")
        print()
    
    print("💡 ملاحظات مهمة:")
    print("   • يجب كتابة الاسم بالضبط كما هو مسجل في النظام")
    print("   • يمكن للطلاب الدخول من أي جهاز متصل بنفس الشبكة")
    print("   • النتائج تُحفظ تلقائياً في النظام")
    print("   • يمكن للمعلم مراجعة النتائج من لوحة التحكم")

def main():
    """الدالة الرئيسية"""
    
    print("🎓 منصة المسابقات الرياضية - التحقق من الطلاب")
    print("=" * 60)
    print()
    
    try:
        # التحقق من الطلاب الجدد
        found, missing = verify_new_students()
        
        # عرض جميع طلاب المستوى
        all_students = show_grade_8_group_1_students()
        
        # إنشاء معلومات الوصول
        generate_student_access_info()
        
        print("\n" + "=" * 60)
        print("🎉 تم التحقق بنجاح!")
        
        if len(found) == 2:
            print("✅ تم إضافة جميع الطلاب المطلوبين بنجاح")
            print("🌐 الطلاب جاهزون للدخول إلى المنصة")
        elif len(found) > 0:
            print(f"⚠️  تم إضافة {len(found)} من أصل 2 طالب")
        else:
            print("❌ لم يتم إضافة أي طالب")
        
        return True
        
    except Exception as e:
        print(f"❌ حدث خطأ: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ تم التحقق بنجاح")
    else:
        print("\n❌ فشل في التحقق")
        sys.exit(1)
